import feedparser
import json
import os
import hashlib
import re
import time
from datetime import datetime, timezone

from sources import ALL_FEEDS, RELEVANCE_KEYWORDS_NL, RELEVANCE_KEYWORDS_EN

ARCHIVE_FILE = os.path.join("cache", "articles.json")
META_FILE = os.path.join("cache", "meta.json")
CACHE_TTL_SECONDS = 6 * 3600  # Refresh at most every 6 hours


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "").strip()


def _parse_date(entry) -> datetime | None:
    for field in ("published_parsed", "updated_parsed", "created_parsed"):
        val = getattr(entry, field, None)
        if val:
            try:
                return datetime(*val[:6], tzinfo=timezone.utc)
            except Exception:
                continue
    return None


def _is_relevant(article: dict) -> bool:
    """Filter articles from general feeds by relevance keywords."""
    text = (article["title"] + " " + article["summary"]).lower()
    keywords = RELEVANCE_KEYWORDS_NL if article["language"] == "nl" else RELEVANCE_KEYWORDS_EN
    return any(kw.lower() in text for kw in keywords)


def _parse_feed(feed_config: dict) -> list[dict]:
    articles = []
    try:
        parsed = feedparser.parse(feed_config["url"])
        for entry in parsed.entries:
            pub = _parse_date(entry)
            if not pub:
                continue

            title = _strip_html(entry.get("title", "")).strip()
            summary = _strip_html(entry.get("summary", entry.get("description", ""))).strip()
            link = entry.get("link", "")

            if not title or not link:
                continue

            article = {
                "id": hashlib.md5(link.encode()).hexdigest(),
                "title": title,
                "summary": summary[:800],
                "link": link,
                "published": pub.isoformat(),
                "source": feed_config["name"],
                "language": feed_config["language"],
            }

            if feed_config.get("filter") and not _is_relevant(article):
                continue

            articles.append(article)
    except Exception as e:
        print(f"[fetcher] Error fetching {feed_config['name']}: {e}")
    return articles


def load_archive() -> list[dict]:
    if os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_archive(articles: list[dict]) -> None:
    os.makedirs("cache", exist_ok=True)
    with open(ARCHIVE_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)


def _get_meta() -> dict:
    if os.path.exists(META_FILE):
        with open(META_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_meta(meta: dict) -> None:
    os.makedirs("cache", exist_ok=True)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f)


def get_last_updated() -> str | None:
    meta = _get_meta()
    ts = meta.get("last_fetched")
    if ts:
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        return dt.strftime("%d-%m-%Y %H:%M UTC")
    return None


def fetch_all(force: bool = False) -> list[dict]:
    """
    Fetch from all feeds and merge into the on-disk archive.
    Respects CACHE_TTL_SECONDS unless force=True.
    Returns the full archive.
    """
    meta = _get_meta()
    last_fetched = meta.get("last_fetched", 0)

    if not force and (time.time() - last_fetched) < CACHE_TTL_SECONDS:
        return load_archive()

    print("[fetcher] Fetching fresh articles from all feeds...")
    archive = {a["id"]: a for a in load_archive()}

    new_count = 0
    for feed_config in ALL_FEEDS:
        fetched = _parse_feed(feed_config)
        for article in fetched:
            if article["id"] not in archive:
                archive[article["id"]] = article
                new_count += 1

    articles = list(archive.values())
    _save_archive(articles)
    _save_meta({"last_fetched": time.time()})

    print(f"[fetcher] Done. {new_count} new articles. {len(articles)} total in archive.")
    return articles
