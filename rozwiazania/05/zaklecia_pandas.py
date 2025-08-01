import pandas as pd

# odczyt pliku XLSX do DataFrame
df = pd.read_excel("zaklecia.xlsx")

print(df)

# dodanie nowego wiersza
nowy_wiersz = {"Zaklęcie": "Expelliarmus", "Efekt": "Rozbrojenie"}
df = df._append(nowy_wiersz, ignore_index=True)

# zapis do nowego pliku
df.to_excel("nowe_zaklecia.xlsx", index=False)

# sprawdzenie
print('------')
print(df)