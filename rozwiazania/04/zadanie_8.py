import bezpieczne_pliki

# test zapisu
wynik_zapisu = bezpieczne_pliki.bezpieczny_zapis("test.txt", "Zaklęcie: Lumos\nZaklęcie: Accio")
print(wynik_zapisu)

# test odczytu
wynik_odczytu = bezpieczne_pliki.bezpieczny_odczyt("test.txt")
print("Zawartość pliku:")
print(wynik_odczytu)
