from sources import DESTEP_KEYWORDS, DESTEP_CATEGORIES


def _score(text: str, keywords: list[str]) -> int:
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw.lower() in text_lower)


def classify_article(article: dict) -> str:
    """Return the DESTEP category with the highest keyword score."""
    text = article["title"] + " " + article["summary"]
    scores = {
        cat: _score(text, DESTEP_KEYWORDS[cat])
        for cat in DESTEP_CATEGORIES
    }
    best = max(scores, key=scores.get)
    # Return "Overig" if no keywords matched at all
    if scores[best] == 0:
        return "Overig"
    return best


def classify_articles(articles: list[dict]) -> dict[str, list[dict]]:
    """Return a dict mapping each DESTEP category to its list of articles."""
    result: dict[str, list[dict]] = {cat: [] for cat in DESTEP_CATEGORIES}
    result["Overig"] = []
    for article in articles:
        cat = classify_article(article)
        result[cat].append(article)
    return result
