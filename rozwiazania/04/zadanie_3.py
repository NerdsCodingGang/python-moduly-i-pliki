with open("wpisy.csv", "r", encoding="utf-8") as plik:
    zawartosc = plik.readlines()

wydarzenia = []   # lista list  [rok, nazwa wydarzenia]
lata = []         # lista lat

for linia in zawartosc:
    if linia.strip() != "":
        czesci = linia.strip().split(",")
        nazwa = czesci[0]
        rok = int(czesci[1])
        wydarzenia.append([rok, nazwa])
        lata.append(rok)

najstarszy = min(lata)
najnowszy = max(lata)

for rok, nazwa in wydarzenia:
    if rok == najstarszy:
        print(f"Najstarszy: {rok} r. {nazwa}")
    if rok == najnowszy:
        print(f"Najnowszy: {rok} r. {nazwa}")
