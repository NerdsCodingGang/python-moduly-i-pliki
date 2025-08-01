import os

def bezpieczny_odczyt(nazwa_pliku):
    if os.path.exists(nazwa_pliku) and os.path.getsize(nazwa_pliku) > 0:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return plik.read()
    else:
        return "Brak danych lub plik nie istnieje."

def bezpieczny_zapis(nazwa_pliku, dane):
    if os.path.exists(nazwa_pliku):
        decyzja = input(f"Plik {nazwa_pliku} już istnieje. Nadpisać? T / N): ")
        
        if decyzja.lower() != "t":
            return "Plik nie został nadpisany." 
            # return przerwie nam wykonywanie tego kodu w tym miejscu i wróci do funkcji 
            # dlatego nie przejdziemy dalej do zapisu
    
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        plik.write(dane)
    return f"Zapisano dane do pliku {nazwa_pliku}"