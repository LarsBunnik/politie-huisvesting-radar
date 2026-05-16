DIRECT_FEEDS = [
    {"url": "https://feeds.nos.nl/nosnieuwsalgemeen", "name": "NOS", "language": "nl", "filter": True},
    {"url": "https://www.nu.nl/rss/Algemeen", "name": "Nu.nl", "language": "nl", "filter": True},
    {"url": "https://feeds.bbci.co.uk/news/world/rss.xml", "name": "BBC World", "language": "en", "filter": True},
    {"url": "https://www.theguardian.com/world/rss", "name": "The Guardian", "language": "en", "filter": True},
]

# Google News RSS search feeds — already topically filtered
SEARCH_FEEDS = [
    {
        "url": "https://news.google.com/rss/search?q=politie+huisvesting+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Huisvesting",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=rijksvastgoed+overheidsgebouw&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Rijksvastgoed",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=woningmarkt+nederland+beleid&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Woningmarkt",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=omgevingswet+vastgoed+bouwvergunning&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Omgevingswet",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=duurzaam+bouwen+kantoor+overheid&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Duurzaam Bouwen",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=hybride+werken+kantoor+overheid+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Hybride Werken",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=woningbouw+stikstof+bouwkosten+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Woningbouw",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=politie+personeel+arbeidsmarkt+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Arbeidsmarkt",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=klimaat+vastgoed+energietransitie+gebouw&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Klimaat Vastgoed",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=geopolitics+housing+europe+policy&hl=en&gl=NL&ceid=NL:en",
        "name": "GNews: Geopolitics Housing",
        "language": "en",
        "filter": False,
    },
]

ALL_FEEDS = DIRECT_FEEDS + SEARCH_FEEDS

# Keywords used to filter articles from general feeds (NOS, Nu.nl, BBC)
RELEVANCE_KEYWORDS_NL = [
    "huisvesting", "vastgoed", "kantoor", "werkplek", "gebouw", "pand", "locatie",
    "politiebureau", "politie", "kazerne", "bureau",
    "woningmarkt", "huurmarkt", "woningbouw", "huurwoning", "wonen", "woning",
    "bouwkosten", "stikstof", "nieuwbouw", "renovatie", "bouw",
    "duurzaam", "energielabel", "verduurzaming", "klimaat",
    "omgevingswet", "bestemmingsplan", "bouwvergunning",
    "hybride werken", "thuiswerken",
    "rijksvastgoed", "overheidsgebouw",
    "bezuinigingen", "budget", "financiering", "investering",
    "arbeidsmarkt", "personeelstekort",
]

RELEVANCE_KEYWORDS_EN = [
    "housing", "real estate", "property", "office", "workplace", "building",
    "construction", "urban planning", "sustainability", "climate",
    "geopolitical", "migration", "inflation", "interest rate",
    "remote work", "hybrid work",
    "government", "policy", "regulation",
]

DESTEP_CATEGORIES = [
    "Demografisch",
    "Economisch",
    "Sociaal-cultureel",
    "Technologisch",
    "Ecologisch",
    "Politiek-juridisch",
]

DESTEP_DESCRIPTIONS = {
    "Demografisch": "Bevolkingsontwikkelingen, vergrijzing, migratie en arbeidsmarkt die de behoefte aan politielocaties beïnvloeden.",
    "Economisch": "Economische trends, bouwkosten, vastgoedmarkt en budgettaire ontwikkelingen.",
    "Sociaal-cultureel": "Maatschappelijke veranderingen, hybride werken, veiligheid en leefbaarheid.",
    "Technologisch": "Digitalisering, smart buildings, innovaties in bouw en werkprocessen.",
    "Ecologisch": "Klimaat, duurzaamheid, energietransitie en milieuregelgeving.",
    "Politiek-juridisch": "Wet- en regelgeving, overheidsbeleid, omgevingswet en politieke besluitvorming.",
}

DESTEP_COLORS = {
    "Demografisch": "#4E79A7",
    "Economisch": "#F28E2B",
    "Sociaal-cultureel": "#E15759",
    "Technologisch": "#76B7B2",
    "Ecologisch": "#59A14F",
    "Politiek-juridisch": "#B07AA1",
}

DESTEP_KEYWORDS = {
    "Demografisch": [
        "bevolkingsgroei", "vergrijzing", "urbanisatie", "migratie", "immigratie",
        "bevolking", "demografie", "arbeidsmarkt", "personeelstekort", "werknemers",
        "leeftijd", "generatie", "jongeren", "senioren", "huishouden",
        "bevolkingskrimp", "inwoners", "prognose", "forecast", "demografisch",
        "population", "migration", "workforce", "aging",
    ],
    "Economisch": [
        "economie", "budget", "bezuinigingen", "inflatie", "bouwkosten", "vastgoedmarkt",
        "rente", "financiering", "investering", "kosten", "prijs", "markt",
        "hypotheek", "huurprijs", "woz", "grondprijs", "aanbesteding",
        "rijksbegroting", "financieel", "subsidie", "fonds", "economisch",
        "economy", "inflation", "interest rate", "investment", "budget",
    ],
    "Sociaal-cultureel": [
        "hybride werken", "thuiswerken", "werkplek", "werkbeleving", "cultuur",
        "diversiteit", "inclusie", "veiligheid", "criminaliteit", "leefbaarheid",
        "gemeenschap", "buurt", "wijk", "sociale cohesie", "welzijn",
        "arbeidsomstandigheden", "flexwerken", "kantoor", "samenwerking",
        "remote work", "hybrid", "culture", "safety", "community",
    ],
    "Technologisch": [
        "digitalisering", "smart building", "technologie", "innovatie", "ai",
        "kunstmatige intelligentie", "automatisering", "sensor", "iot", "data",
        "digitaal", "robotica", "bim", "prefab", "modulair bouwen",
        "digital twin", "energiemanagementsysteem", "gebouwautomatisering",
        "technology", "digital", "automation", "smart",
    ],
    "Ecologisch": [
        "klimaat", "duurzaam bouwen", "energietransitie", "co2", "circulariteit",
        "biodiversiteit", "stikstof", "milieu", "duurzaamheid", "energielabel",
        "beng", "nul-op-de-meter", "zonnepanelen", "warmtepomp", "isolatie",
        "klimaatakkoord", "verduurzaming", "groen", "natuur", "ecologisch",
        "climate", "sustainability", "green", "emissions", "renewable",
    ],
    "Politiek-juridisch": [
        "wet- en regelgeving", "overheidsbeleid", "bestemmingsplan", "omgevingswet",
        "rijksvastgoed", "beleid", "wetgeving", "gemeente", "provincie", "rijk",
        "minister", "kabinet", "coalitie", "politiek", "partij", "verkiezing",
        "besluit", "vergunning", "handhaving", "inspectie", "toezicht",
        "law", "regulation", "policy", "government", "parliament",
    ],
}
