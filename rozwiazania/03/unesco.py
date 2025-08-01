import requests

API_URL = "https://api.zabytek.gov.pl/nidrestapi/api/data/geoportal/otwarteDaneZestawienieUn?format=json"

def pobierz_dane():
    """pobiera dane z API i zwraca listę zabytków"""
    response = requests.get(API_URL)
    data = response.json()
    return data["data"]  # zakładamy, że lista jest w kluczu 'data'

def znajdz_nowsze(dane, rok):
    """zwraca zabytki wpisane po podanym roku"""
    wynik = []
    for zabytek in dane:
        if int(zabytek["dataWpisu"]) > rok:
            wynik.append(zabytek)
    return wynik

def znajdz_starsze(dane, rok):
    """opcjonalnie: zwraca zabytki wpisane przed podanym rokiem"""
    wynik = []
    for zabytek in dane:
        if int(zabytek["dataWpisu"]) < rok:
            wynik.append(zabytek)
    return wynik

def filtruj_po_wojewodztwie(dane, wojewodztwo):
    """zwraca zabytki z wybranego województwa"""
    wynik = []
    for zabytek in dane:
        if zabytek["wojewodztwo"].lower() == wojewodztwo.lower():
            wynik.append(zabytek)
    return wynik
