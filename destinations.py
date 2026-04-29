"""Belfast International Airport (BFS) destinations — April 2026."""

DESTINATIONS = {
    "BFS": {
        "name": "Belfast International",
        "routes": {
            "ACE": "Lanzarote",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "AYT": "Antalya",
            "BCN": "Barcelona",
            "BGY": "Milan Bergamo",
            "BHX": "Birmingham",
            "BOD": "Bordeaux",
            "BRS": "Bristol",
            "CDG": "Paris CDG",
            "CGN": "Cologne Bonn",
            "CUN": "Cancun",
            "DBV": "Dubrovnik",
            "DLM": "Dalaman",
            "EDI": "Edinburgh",
            "EMA": "East Midlands",
            "FAO": "Faro",
            "FUE": "Fuerteventura",
            "GLA": "Glasgow",
            "GRO": "Girona",
            "HRG": "Hurghada",
            "JER": "Jersey",
            "KRK": "Krakow",
            "LBA": "Leeds Bradford",
            "LCA": "Larnaca",
            "LGW": "London Gatwick",
            "LPA": "Gran Canaria",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "MLA": "Malta",
            "NCL": "Newcastle",
            "OPO": "Porto",
            "PMI": "Palma",
            "REU": "Reus",
            "SOU": "Southampton",
            "STN": "London Stansted",
            "TFS": "Tenerife South",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
