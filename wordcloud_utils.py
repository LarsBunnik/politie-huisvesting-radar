import io
import re
from collections import Counter

from PIL import Image
from wordcloud import WordCloud

# Dutch + English stop words
STOP_WORDS = {
    # Dutch
    "de", "het", "een", "en", "van", "in", "is", "dat", "op", "te", "zijn", "met",
    "voor", "aan", "niet", "ook", "er", "maar", "om", "dit", "zo", "bij", "nog",
    "al", "dan", "naar", "uit", "door", "over", "ze", "hij", "we", "u", "ze",
    "meer", "al", "als", "nu", "kan", "die", "worden", "heeft", "worden", "heeft",
    "dit", "nog", "na", "tot", "werd", "jaar", "nieuwe", "twee", "wel", "zeer",
    "geen", "andere", "echter", "veel", "meer", "moet", "mee", "hem", "zijn",
    "hebben", "wordt", "hun", "hoe", "wat", "wie", "waar", "wanneer", "omdat",
    "worden", "waren", "bij", "hun", "hier", "daar", "dus", "toch", "ook",
    "reeds", "juist", "steeds", "verder", "binnen", "buiten", "zelf", "zeker",
    "goed", "groot", "klein", "hoog", "laag", "lang", "kort", "samen",
    # English
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "shall", "can", "need",
    "this", "that", "these", "those", "it", "its", "they", "them", "their",
    "he", "she", "we", "you", "i", "my", "your", "our", "his", "her",
    "not", "no", "nor", "so", "yet", "both", "either", "neither", "each",
    "more", "most", "other", "some", "such", "than", "too", "very",
    "just", "also", "new", "year", "says", "said", "after", "first",
    # Common news words that add no signal
    "reuters", "bbc", "nos", "nu", "google", "nieuws", "news", "artikel",
    "lees", "lezen", "bekijk", "meer", "verder",
    # HTML entity remnants
    "nbsp", "amp", "quot", "apos", "lt", "gt",
}


def _tokenize(text: str) -> list[str]:
    tokens = re.findall(r"\b[a-zA-ZÀ-ÿ]{3,}\b", text.lower())
    return [t for t in tokens if t not in STOP_WORDS]


def get_word_frequencies(articles: list[dict]) -> Counter:
    tokens = []
    for article in articles:
        tokens.extend(_tokenize(article["title"]))
        tokens.extend(_tokenize(article["summary"]))
    return Counter(tokens)


def generate_wordcloud(articles: list[dict], color: str = "#1f4e79") -> tuple[bytes | None, list[tuple[str, int]]]:
    """
    Generate a word cloud image and return (png_bytes, top_words).
    top_words is a list of (word, frequency) tuples.
    """
    if not articles:
        return None, []

    freq = get_word_frequencies(articles)
    if not freq:
        return None, []

    top_words = freq.most_common(20)

    try:
        wc = WordCloud(
            width=600,
            height=300,
            background_color="white",
            colormap="Blues",
            max_words=60,
            prefer_horizontal=0.85,
            min_font_size=10,
        ).generate_from_frequencies(dict(freq))

        img = wc.to_image()
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue(), top_words

    except Exception as e:
        print(f"[wordcloud] Error: {e}")
        return None, top_words
