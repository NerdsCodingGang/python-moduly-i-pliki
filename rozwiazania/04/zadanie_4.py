import zaklecia

banned_spells = ["avada", "imperi", "crucio"]

with open("ksiega_zaklec.txt", "r", encoding="utf-8") as plik:
    tekst = plik.read()

bezpieczny_tekst = zaklecia.filter_spells(tekst, banned_spells)

print(bezpieczny_tekst)