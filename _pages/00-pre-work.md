---
title: 0. Pre-work
layout: post
---

Ta lekcja jest materiałem powtórkowym, mini-lekcja wyrównawcza. Jest ona zupełnie nie obowiązkowa. Możesz potraktować ją jako ściągę lub wykorzystać do przygotowania się do zajęć. 

## 🐍 Python w pigułce

### 1) Zmienne i typy
📌 Zmienna czyli pudełko na dane. Dane mogą być różnego typu - liczby całkowite, dziesiętne (zmiennoprzecinkowe), teksty czy zmienne typu boolean `True/False`.

```python
wiek = 18          # int – liczba całkowita
srednia = 4.5      # float – liczba zmiennoprzecinkowa
imie = "Ala"       # str – tekst
aktywny = True     # bool – prawda/fałsz

print(type(wiek))  # <class 'int'>
```

### 2) input() i rzutowanie

📌 `input()` zawsze zwraca tekst (`str`).

Jeśli chcesz liczbę, wykonaj rzutowanie z typu tekstowego na liczbowy.
Metoda `type()` pozwala mi podejrzeć typ.

```python
wiek = input("Podaj wiek: ")
print(type(wiek))  # <class 'str'>

wiek = int(input("Podaj wiek: "))
print(type(wiek))  # <class 'int'>

wiek = int(input("Podaj wiek: "))
wiek = float(wiek)  
print(type(wiek))  # <class 'float'>
```

- `int("20")` - zrzutuje tekst "20" na liczbę całkowitą
- `float("20.15")`  - zrzutuje tekst "20" na liczbę float

### 3) Stringi i f‑string + operacje na stringach
📌 String (`str`) to tekst w cudzysłowie lub apostrofach.

- f‑string – wstawianie zmiennych do tekstu

```python
imie = "Ania"
wiek = 18
print(f"{imie} ma {wiek} lat")           # Ania ma 18 lat
print(f"Za rok będzie mieć {wiek + 1}")  # Za rok będzie mieć 19
```

Operacje na stringach
```python
tekst = "Python jest SUPER"

print(tekst.lower())    # python jest super
print(tekst.upper())    # PYTHON JEST SUPER
print(tekst.replace("SUPER", "fajny"))  # Python jest fajny

# Sprawdzenie czy coś jest w tekście
print("Python" in tekst)    # True
print("Java" in tekst)      # False
```

📌 **Warto wiedzi:**

- `.lower()` / `.upper()` - zmieniają wielkość liter
- `.replace(a, b)` zamienia tekst a na b
- `"coś" in tekst` sprawdza, czy w tekście występuje dane słowo

### 4) Instrukcje warunkowe
📌 `if` sprawdza warunek, `elif` kolejne, `else` na końcu.

```python
punkty = int(input("Podaj punkty: "))

if punkty >= 90:
    print("Ocena 5")
elif punkty >= 70:
    print("Ocena 4")
else:
    print("Ocena 3 lub mniej")
```

5) Pętla for
📌 `for` powtarza kod określoną liczbę razy lub dla elementów listy.
`range()` liczy od zera.

```python
for i in range(5):
    print(i)  # 0,1,2,3,4

owoce = ["jabłko", "banan", "gruszka"]
for owoc in owoce:
    print(owoc)
```

### 6) Pętla while
📌 `while` działa tak długo, jak warunek jest `True`.

```python
while True:
    liczba = int(input("Podaj liczbę (0 aby zakończyć): "))
    if liczba == 0:
        break
    print(f"Podałeś: {liczba}")

print("Koniec programu, pa pa")
```

### 7) Moduł random
📌 `random.randint(a, b)` losuje liczbę od a do b.

```python
import random

liczba = random.randint(1, 10)
print(f"Wylosowano: {liczba}")
```

### 8) Funkcje
📌 Funkcje przyjmują parametry i mogą działać na różnych danych.

```python
def przywitaj(imie):
    print(f"Cześć, {imie}!")

przywitaj("Ania")
przywitaj("Ola")
```

### 9) Funkcja z parametrami i pętlą
📌 Parametry pozwalają ustawić wartości, pętla powtarza czynność.

```python
def pieski(imie, liczba):
    print(f"{imie} ma urocze pieski:")
    for i in range(liczba):
        print("🐶")

pieski("Ania", 3)
```

### 10) Funkcja z listą i losowaniem emoji
📌 `random.choice()` losuje element z listy.

```python
import random

def przydziel_emoji(lista_imion):
    emoji_lista = ["🐶", "🐷", "🐸"]
    for imie in lista_imion:
        emoji_wylosowane = random.choice(emoji_lista)
        print(f"{imie} dostaje {emoji_wylosowane}")

przydziel_emoji(["Ania", "Ola", "Kasia"])
```

### 📌 Zadanie: „Przepis bez alergenów”

Czas na połączenie wszystkiego: stringi, pętle, funkcje.

Napisz funkcję `remove_allergens(text, ingredients)`, która:
- przyjmuje opis przepisu (text) oraz listę alergenów (ingredients)
- usuwa alergeny z tekstu (ignorując wielkość liter)
- zwraca nową, „bezpieczną” wersję przepisu

Stwórz listę kilku przepisów (każdy jako string)

```python
przepisy = [
    "Ciasto z jajkami i mlekiem",
    "Sałatka z pomidorem i orzechami włoskimi",
    "Makaron z glutenem i sosem pomidorowym",
    "Orzechowy ramen"
]

```

Użyj pętli, aby przefiltrować wszystkie przepisy i wyświetlić wersje bez alergenów

![]({{ site.baseurl }}/assets/food.gif)

Przykład rozwiązania:

```python
def remove_allergens(text, ingredients):
    text_lower = text.lower()
    for alergen in ingredients:
        text_lower = text_lower.replace(alergen.lower(), "[usunięto]")
    return text_lower

przepisy = [
    "Ciasto z jajkami i mlekiem",
    "Sałatka z orzechami i pomidorem",
    "Makaron z glutenem i sosem pomidorowym"
]

alergeny = ["jajka", "mleko", "orzechy", "gluten"]

for przepis in przepisy:
    print(remove_allergens(przepis, alergeny))

```

✅ Przykładowy wynik:

```
ciasto z [usunięto] i [usunięto]
sałatka z [usunięto] i pomidorem
makaron z [usunięto] i sosem pomidorowym
```