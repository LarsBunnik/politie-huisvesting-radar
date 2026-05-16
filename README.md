# Politie Huisvesting Radar

Kwartaallijks nieuwsoverzicht voor de strategisch adviseurs Huisvesting van de Politie Nederland.

Volgt externe trends die van invloed zijn op het toekomstige vastgoedportfolio, geclassificeerd via de **DESTEP-methode**.

## Functies

- Haalt nieuws op uit Nederlandse en internationale bronnen (NOS, Nu.nl, Google News, BBC)
- Classificeert artikelen automatisch in DESTEP-categorieën
- Woordwolk per categorie met klikbare trefwoorden
- Klikbare links naar onderliggende nieuwsartikelen
- Schuivende tijdsvensters: 5 jaar → 2 jaar → 1 jaar → per kwartaal
- Archief groeit bij elke run — historische data bouwt op in de loop van de tijd

## Installatie

```bash
pip install -r requirements.txt
```

## Gebruik

```bash
streamlit run app.py
```

Open vervolgens `http://localhost:8501` in je browser.

Klik op **Data verversen** in de zijbalk om de nieuwste artikelen op te halen.

## DESTEP-categorieën

| Categorie | Beschrijving |
|---|---|
| **Demografisch** | Bevolkingsontwikkelingen, vergrijzing, arbeidsmarkt |
| **Economisch** | Bouwkosten, vastgoedmarkt, budgettaire trends |
| **Sociaal-cultureel** | Hybride werken, veiligheid, leefbaarheid |
| **Technologisch** | Digitalisering, smart buildings, innovatie |
| **Ecologisch** | Klimaat, duurzaamheid, energietransitie |
| **Politiek-juridisch** | Wet- en regelgeving, omgevingswet, overheidsbeleid |

## Structuur

```
├── app.py               # Streamlit web app
├── fetcher.py           # RSS ophalen + archief op schijf
├── classifier.py        # DESTEP-classificatie op basis van trefwoorden
├── wordcloud_utils.py   # Woordwolk genereren
├── sources.py           # Bronnen en trefwoorden
├── requirements.txt
└── cache/               # Lokaal archief (wordt niet meegenomen in git)
```
