nazwa_pliku = "krotkie_zaklecia.csv"


with open(nazwa_pliku, "w", encoding="utf-8") as plik:
    # nagłówek
    plik.write("Zaklęcie,Efekt\n")
    
    # 3 zaklęcia od użytkownika - można je zamknąć jako funkcja :)
    for i in range(3):
        zaklecie = input("Podaj zaklęcie: ")
        efekt = input("Podaj efekt: ")
        plik.write(zaklecie + "," + efekt + "\n")

print(f"Dane zapisano do pliku {nazwa_pliku}")