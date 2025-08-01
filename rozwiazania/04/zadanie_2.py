with open("wpisy.txt", "r", encoding="utf-8") as fp:
    zawartosc = fp.readlines()

lata = []
for linia in zawartosc:
    if linia.strip() != "":
        lata.append(int(linia.strip()))

print("Najstarszy rok:", min(lata))
print("Najnowszy rok:", max(lata))