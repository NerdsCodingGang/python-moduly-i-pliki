import unesco

if __name__ == "__main__":
    # pobierz dane
    dane = unesco.pobierz_dane()
    print("Pobrano dane o zabytkach UNESCO.\n")

    # ---- filtrowanie po dacie ----
    rok = int(input("Podaj rok (np. 2000): "))
    nowsze = unesco.znajdz_nowsze(dane, rok)

    if nowsze:
        print(f"\nZabytki wpisane po roku {rok}:")
        for z in nowsze:
            print(f"{z['nazwa']} - {z['dataWpisu']} - {z['miejscowosc']} ({z['wojewodztwo']})")
    else:
        print(f"\nNie znaleziono zabytków wpisanych po roku {rok}.")

    # ---- filtrowanie po województwie ----
    woj = input("\nPodaj województwo: ")
    lista = unesco.filtruj_po_wojewodztwie(dane, woj)

    if lista:
        print(f"\nZabytki w województwie {woj}:")
        for z in lista:
            print(f"{z['nazwa']} - {z['dataWpisu']} - {z['miejscowosc']} ({z['wojewodztwo']})")
    else:
        print(f"\nNie znaleziono zabytków w województwie {woj}.")
