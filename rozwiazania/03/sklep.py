magazyn = {
    "Czekoladowa żaba": 10,
    "Maślane piwo": 7,
    "Pióro feniksa": 50
}

def kup(produkt, galeony):
    if produkt in magazyn:
        cena = magazyn[produkt]
        if galeony >= cena:
            reszta = galeony - cena
            return f"Kupiłeś {produkt}! Zostało Ci {reszta} galeonów."
        else:
            return f"Nie stać Cię na {produkt}!"
    else:
        return "Taki produkt nie istnieje w sklepie."
