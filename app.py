import streamlit as st
from datetime import datetime, timedelta, timezone

from fetcher import fetch_all, get_last_updated
from classifier import classify_articles
from wordcloud_utils import generate_wordcloud
from sources import DESTEP_CATEGORIES, DESTEP_DESCRIPTIONS, DESTEP_COLORS

st.set_page_config(
    page_title="Politie Huisvesting Radar",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .stExpander > div:first-child { font-size: 0.95rem; }
    .article-meta { color: #666; font-size: 0.82rem; }
    .category-badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Politie_logo.svg/200px-Politie_logo.svg.png", width=120)
    st.title("Huisvesting Radar")
    st.caption("Strategisch nieuwsoverzicht voor vastgoedbeleid Politie Nederland")
    st.divider()

    if st.button("🔄 Data verversen", use_container_width=True):
        st.cache_data.clear()
        with st.spinner("Nieuws ophalen van alle bronnen..."):
            articles = fetch_all(force=True)
        st.success(f"✓ {len(articles)} artikelen in archief")

    last_updated = get_last_updated()
    if last_updated:
        st.caption(f"Laatste update: {last_updated}")

    st.divider()
    st.subheader("Tijdsvenster")

    window_choice = st.radio(
        "Periode",
        options=["5 jaar", "2 jaar", "1 jaar", "Per kwartaal"],
        index=2,
        label_visibility="collapsed",
    )

    selected_quarter = None
    if window_choice == "Per kwartaal":
        now = datetime.now(timezone.utc)
        quarters = []
        for i in range(8):
            d = now - timedelta(days=i * 91)
            q = (d.month - 1) // 3 + 1
            label = f"Q{q} {d.year}"
            if label not in quarters:
                quarters.append(label)
        selected_quarter = st.selectbox("Kwartaal", quarters)

    st.divider()
    st.caption("**Over DESTEP**")
    for cat, desc in DESTEP_DESCRIPTIONS.items():
        color = DESTEP_COLORS[cat]
        st.markdown(
            f'<span style="color:{color}; font-weight:600;">● {cat}</span><br>'
            f'<span style="font-size:0.78rem; color:#555;">{desc}</span>',
            unsafe_allow_html=True,
        )
        st.write("")


# ── Load & filter articles ────────────────────────────────────────────────────

@st.cache_data(ttl=3600, show_spinner=False)
def load_articles():
    return fetch_all(force=False)


with st.spinner("Archief laden..."):
    all_articles = load_articles()

now = datetime.now(timezone.utc)

if window_choice == "Per kwartaal" and selected_quarter:
    q_num = int(selected_quarter[1])
    q_year = int(selected_quarter[3:])
    q_start = datetime(q_year, (q_num - 1) * 3 + 1, 1, tzinfo=timezone.utc)
    q_end = q_start + timedelta(days=92)
    window_articles = [
        a for a in all_articles
        if q_start <= datetime.fromisoformat(a["published"]) < q_end
    ]
    period_label = selected_quarter
else:
    days_map = {"5 jaar": 5 * 365, "2 jaar": 2 * 365, "1 jaar": 365}
    cutoff = now - timedelta(days=days_map[window_choice])
    window_articles = [
        a for a in all_articles
        if datetime.fromisoformat(a["published"]) >= cutoff
    ]
    period_label = window_choice


# ── Header ────────────────────────────────────────────────────────────────────

st.title("🏛️ Politie Huisvesting Radar")

col_h1, col_h2, col_h3 = st.columns(3)
col_h1.metric("Artikelen in venster", len(window_articles))
col_h2.metric("Totaal in archief", len(all_articles))
col_h3.metric("Periode", period_label)

if not window_articles:
    st.warning(
        "Geen artikelen gevonden voor dit tijdsvenster. "
        "Klik op **Data verversen** in de zijbalk of kies een ruimer venster."
    )
    st.stop()

classified = classify_articles(window_articles)

st.divider()


# ── DESTEP Tabs ───────────────────────────────────────────────────────────────

tab_labels = [
    f"{cat.split('-')[0]} ({len(classified.get(cat, []))})"
    for cat in DESTEP_CATEGORIES
]
tabs = st.tabs(tab_labels)

for tab, category in zip(tabs, DESTEP_CATEGORIES):
    with tab:
        cat_articles = classified.get(category, [])
        color = DESTEP_COLORS[category]

        st.markdown(
            f'<span class="category-badge" style="background:{color}20; color:{color};">'
            f'{category}</span> &nbsp; {DESTEP_DESCRIPTIONS[category]}',
            unsafe_allow_html=True,
        )

        if not cat_articles:
            st.info("Geen artikelen in deze categorie voor het geselecteerde tijdsvenster.")
            continue

        col_wc, col_articles = st.columns([2, 3], gap="large")

        # ── Word cloud ──────────────────────────────────────────────────────
        with col_wc:
            st.subheader("Woordwolk")
            wc_image, top_words = generate_wordcloud(cat_articles, color=color)

            if wc_image:
                st.image(wc_image, use_container_width=True)
            else:
                st.info("Te weinig tekst voor woordwolk.")

            if top_words:
                st.caption("**Klik op een trefwoord** om de artikellijst te filteren:")

                filter_key = f"filter_{category}"
                if filter_key not in st.session_state:
                    st.session_state[filter_key] = None

                # Show top words as clickable buttons in a 4-column grid
                word_cols = st.columns(4)
                for i, (word, _freq) in enumerate(top_words[:16]):
                    is_active = st.session_state[filter_key] == word
                    btn_label = f"**{word}**" if is_active else word
                    if word_cols[i % 4].button(
                        btn_label,
                        key=f"wbtn_{category}_{word}",
                        use_container_width=True,
                        type="primary" if is_active else "secondary",
                    ):
                        st.session_state[filter_key] = None if is_active else word
                        st.rerun()

                if st.session_state[filter_key]:
                    if st.button("✕ Filter wissen", key=f"clear_{category}"):
                        st.session_state[filter_key] = None
                        st.rerun()

        # ── Article list ────────────────────────────────────────────────────
        with col_articles:
            active_filter = st.session_state.get(f"filter_{category}")

            if active_filter:
                display_articles = [
                    a for a in cat_articles
                    if active_filter.lower() in (a["title"] + " " + a["summary"]).lower()
                ]
                st.subheader(f"Artikelen over '{active_filter}' ({len(display_articles)})")
            else:
                display_articles = cat_articles
                st.subheader(f"Alle artikelen ({len(display_articles)})")

            sorted_articles = sorted(
                display_articles,
                key=lambda x: x["published"],
                reverse=True,
            )

            if not sorted_articles:
                st.info(f"Geen artikelen gevonden met het trefwoord '{active_filter}'.")
            else:
                for article in sorted_articles:
                    pub = datetime.fromisoformat(article["published"])
                    pub_str = pub.strftime("%d %b %Y")
                    source = article["source"].replace("GNews: ", "")

                    with st.expander(f"{article['title']}"):
                        st.markdown(
                            f'<p class="article-meta">📰 {source} &nbsp;·&nbsp; 📅 {pub_str}</p>',
                            unsafe_allow_html=True,
                        )
                        if article["summary"]:
                            st.write(article["summary"])
                        st.markdown(f"[🔗 Lees het volledige artikel →]({article['link']})")


# ── Footer ────────────────────────────────────────────────────────────────────

st.divider()
st.caption(
    "Politie Huisvesting Radar · Beleidsmakers & Strategisch Adviseurs Huisvesting · "
    "Archief groeit met elke run · Bronnen: NOS, Nu.nl, Google News, BBC, The Guardian"
)
