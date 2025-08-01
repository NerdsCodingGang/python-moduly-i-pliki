import csv

with open("zaklecia.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik)
    for wiersz in czytnik:
        print(wiersz)