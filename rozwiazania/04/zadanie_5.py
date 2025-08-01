import random

liczba = random.randint(1, 100)
print(f"Wylosowana liczba: {liczba}")

nazwa_pliku = input("Podaj nazwę pliku (z rozszerzeniem .txt): ")

with open(nazwa_pliku, "w", encoding="utf-8") as plik:
    plik.write("❤︎" * liczba)

print(f"Zapisano {liczba} ❤︎ do pliku {nazwa_pliku}")