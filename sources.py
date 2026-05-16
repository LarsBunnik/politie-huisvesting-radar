DIRECT_FEEDS = [
    # Dutch general news — filtered by relevance keywords
    {"url": "https://feeds.nos.nl/nosnieuwsalgemeen", "name": "NOS Algemeen", "language": "nl", "filter": True},
    {"url": "https://feeds.nos.nl/nosnieuwspolitiek", "name": "NOS Politiek", "language": "nl", "filter": True},
    {"url": "https://www.nu.nl/rss/Algemeen", "name": "Nu.nl", "language": "nl", "filter": True},
    {"url": "https://www.rtlnieuws.nl/rss.xml", "name": "RTL Nieuws", "language": "nl", "filter": True},
    # Authoritative government & sector sources — already on-topic, no filtering needed
    {"url": "https://www.rijksoverheid.nl/rss", "name": "Rijksoverheid", "language": "nl", "filter": False},
    {"url": "https://www.binnenlandsbestuur.nl/rss", "name": "Binnenlands Bestuur", "language": "nl", "filter": False},
    {"url": "https://www.cobouw.nl/rss", "name": "Cobouw", "language": "nl", "filter": False},
    {"url": "https://www.vastgoedmarkt.nl/rss", "name": "Vastgoedmarkt", "language": "nl", "filter": False},
    # International — major geopolitical signal only
    {"url": "https://feeds.bbci.co.uk/news/world/rss.xml", "name": "BBC World", "language": "en", "filter": True},
]

# Google News RSS search feeds — already topically filtered
SEARCH_FEEDS = [
    # Police-specific
    {
        "url": "https://news.google.com/rss/search?q=politiebureau+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politiebureau",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=politie+huisvesting+vastgoed&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Huisvesting",
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
        "url": "https://news.google.com/rss/search?q=politie+digitalisering+technologie+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Technologie",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=politie+bezuinigingen+budget+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Budget",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=politie+duurzaamheid+gebouw&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Politie Duurzaamheid",
        "language": "nl",
        "filter": False,
    },
    # Government real estate
    {
        "url": "https://news.google.com/rss/search?q=rijksvastgoed+overheidsgebouw+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Rijksvastgoed",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=overheid+kantoor+werkplek+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Overheid Kantoor",
        "language": "nl",
        "filter": False,
    },
    # Housing market & construction
    {
        "url": "https://news.google.com/rss/search?q=woningmarkt+nederland+beleid+2025&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Woningmarkt",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=omgevingswet+bestemmingsplan+bouw&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Omgevingswet",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=woningbouw+stikstof+bouwkosten+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Woningbouw",
        "language": "nl",
        "filter": False,
    },
    # Sustainability & workplace
    {
        "url": "https://news.google.com/rss/search?q=duurzaam+bouwen+kantoor+overheid+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Duurzaam Bouwen",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=hybride+werken+overheid+kantoor+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Hybride Werken",
        "language": "nl",
        "filter": False,
    },
    {
        "url": "https://news.google.com/rss/search?q=klimaat+vastgoed+energietransitie+gebouw+nederland&hl=nl&gl=NL&ceid=NL:nl",
        "name": "GNews: Klimaat Vastgoed",
        "language": "nl",
        "filter": False,
    },
    # International signal
    {
        "url": "https://news.google.com/rss/search?q=geopolitics+europe+housing+policy&hl=en&gl=NL&ceid=NL:en",
        "name": "GNews: Geopolitics Housing",
        "language": "en",
        "filter": False,
    },
]

ALL_FEEDS = DIRECT_FEEDS + SEARCH_FEEDS

# Keywords used to filter articles from general feeds (NOS, Nu.nl, RTL, BBC)
RELEVANCE_KEYWORDS_NL = [
    # Police-specific
    "politie", "politiebureau", "politiepost", "kazerne", "politiekorps",
    "nationale politie", "korps", "agent", "recherche", "arrestantenzorg",
    # Real estate & buildings
    "huisvesting", "vastgoed", "kantoor", "werkplek", "gebouw", "pand", "locatie",
    "rijksvastgoed", "overheidsgebouw", "servicecentrum",
    # Housing market & construction
    "woningmarkt", "huurmarkt", "woningbouw", "huurwoning", "wonen", "woning",
    "bouwkosten", "stikstof", "nieuwbouw", "renovatie", "bouw", "bestemmingsplan",
    # Sustainability
    "duurzaam", "energielabel", "verduurzaming", "klimaat", "energietransitie",
    # Regulations
    "omgevingswet", "bouwvergunning", "regelgeving",
    # Work & organisation
    "hybride werken", "thuiswerken", "flexwerken",
    # Finance
    "bezuinigingen", "budget", "financiering", "investering", "rijksbegroting",
    # Labour
    "arbeidsmarkt", "personeelstekort", "werving", "instroom",
]

RELEVANCE_KEYWORDS_EN = [
    "housing", "real estate", "property", "office", "workplace", "building",
    "construction", "urban planning", "sustainability", "climate",
    "geopolitical", "migration", "inflation", "interest rate",
    "remote work", "hybrid work", "government", "policy", "regulation",
    "police", "law enforcement",
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
        # General demographics
        "bevolkingsgroei", "vergrijzing", "urbanisatie", "migratie", "immigratie",
        "bevolking", "demografie", "huishouden", "bevolkingskrimp", "inwoners",
        "prognose", "demografisch", "population", "migration", "aging",
        # Police-specific demographics
        "arbeidsmarkt", "personeelstekort", "werknemers", "instroom", "uitstroom",
        "politiepersoneel", "werving", "agenten", "korps", "bezetting",
        "vergrijzing politie", "nieuwe agenten", "politieacademie",
        "leeftijdsopbouw", "generatie", "werkdruk",
    ],
    "Economisch": [
        # General economics
        "economie", "inflatie", "rente", "markt", "hypotheek", "huurprijs",
        "grondprijs", "financieel", "subsidie", "fonds", "economisch",
        "economy", "inflation", "interest rate", "investment",
        # Police/government real estate economics
        "budget", "bezuinigingen", "bouwkosten", "vastgoedmarkt", "financiering",
        "investering", "kosten", "prijs", "woz", "aanbesteding", "rijksbegroting",
        "politiebegroting", "exploitatiekosten", "onderhoud", "renovatiekosten",
        "huurlasten", "vastgoedportefeuille", "businesscase",
    ],
    "Sociaal-cultureel": [
        # General social trends
        "cultuur", "diversiteit", "inclusie", "gemeenschap", "buurt", "wijk",
        "sociale cohesie", "welzijn", "leefbaarheid", "remote work", "hybrid",
        # Police-specific social trends
        "hybride werken", "thuiswerken", "werkplek", "werkbeleving", "flexwerken",
        "samenwerking", "arbeidsomstandigheden", "politiecultuur",
        "veiligheid", "criminaliteit", "onveiligheid", "overlast",
        "wijkagent", "buurtpolitie", "community policing",
        "agressie", "werkplezier", "ziekteverzuim", "stress", "politiewerk",
    ],
    "Technologisch": [
        # General technology
        "technologie", "innovatie", "sensor", "iot", "data", "robotica",
        "technology", "digital", "automation", "smart",
        # Police & building technology
        "digitalisering", "smart building", "ai", "kunstmatige intelligentie",
        "automatisering", "bim", "prefab", "modulair bouwen",
        "digital twin", "energiemanagementsysteem", "gebouwautomatisering",
        "cameratoezicht", "bodycam", "surveillance", "opsporing",
        "datasystemen", "it-systemen", "cloud", "cybersecurity",
        "politietechnologie", "drones", "kentekenscan",
    ],
    "Ecologisch": [
        # General ecology
        "biodiversiteit", "natuur", "ecologisch", "climate", "green", "emissions",
        # Sustainability in buildings & police context
        "klimaat", "duurzaam bouwen", "energietransitie", "co2", "circulariteit",
        "stikstof", "milieu", "duurzaamheid", "energielabel", "renewable",
        "beng", "nul-op-de-meter", "zonnepanelen", "warmtepomp", "isolatie",
        "klimaatakkoord", "verduurzaming", "sustainability",
        "klimaatadaptatie", "wateroverlast", "hittestress",
        "energiebesparing", "gasvrij", "co2-neutraal",
    ],
    "Politiek-juridisch": [
        # General policy & law
        "wetgeving", "gemeente", "provincie", "rijk", "minister", "kabinet",
        "coalitie", "verkiezing", "besluit", "law", "regulation", "parliament",
        # Police & real estate regulations
        "wet- en regelgeving", "overheidsbeleid", "bestemmingsplan", "omgevingswet",
        "rijksvastgoed", "beleid", "vergunning", "handhaving", "inspectie", "toezicht",
        "politiewet", "veiligheidsregio", "ministry", "government",
        "bouwregelgeving", "ruimtelijke ordening", "erfgoed",
        "aanbestedingsrecht", "privacywetgeving", "avg",
        "nationale politie beleid", "politieakkoord",
    ],
}
