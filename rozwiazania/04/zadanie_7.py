import zaklecia

banned_spells = ["avada", "imperi", "crucio"]

with open("ksiega_zaklec.csv", "r", encoding="utf-8") as plik:
    tekst = plik.read()

# filtracja zaklęć
bezpieczny_tekst = zaklecia.filter_spells(tekst, banned_spells)

# zapis oczyszczonych zaklęć do nowego pliku
with open("bezpieczne_zaklecia.csv", "w", encoding="utf-8") as plik:
    plik.write(bezpieczny_tekst)

print("Oczyszczone zaklęcia zapisano do bezpieczne_zaklecia.csv")
