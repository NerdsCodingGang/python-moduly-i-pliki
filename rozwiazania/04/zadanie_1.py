with open("domy.txt", "r", encoding="utf-8") as fp:
    zawartosc = fp.readlines()

# usuwamy puste linie
domy = []
for linia in zawartosc:
    if linia.strip() != "":
        domy.append(linia.strip())

# numerowana lista
for numer, dom in enumerate(domy, start=1):
    print(f"{numer}. {dom}")