import csv

zaklecia = [
    ["Zaklęcie", "Efekt"],
    ["Lumos", "Światło"],
    ["Accio", "Przywołanie przedmiotu"],
    ["Protego", "Tarcza ochronna"]
]

with open("zaklecia_nowe.csv", "w", encoding="utf-8", newline="") as plik:
    zapis = csv.writer(plik)
    zapis.writerows(zaklecia)
    print('✔ Zapisano!')