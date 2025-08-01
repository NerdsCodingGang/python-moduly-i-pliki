---
title: 4. Otwieranie plików
layout: post
---

Do tej pory pracowaliśmy tylko z danymi wpisywanymi w kodzie lub podawanymi przez użytkownika.  
Czas na kolejny krok – **praca z plikami**.  

Python potrafi **czytać pliki** (np. `.txt`, `.csv`, `.json`) i **zapisywać dane** z powrotem do pliku.  
To przydatne, gdy chcemy przechowywać dane między uruchomieniami programu – np. wyniki gry, listę uczniów Hogwartu czy logi punktów domów.

---


Zacznijmy od prostego pliku tekstowego.  

Stwórz plik `zaklecia.txt` z treścią:

```
Alohomora
Wingardium Leviosa
Expelliarmus
...
```

Dodaj więcej zakleć jeśli masz ochotę 


## 📂 Otwieramy pierwszy plik `.txt`

Python ma wbudowaną funkcję **`open()`**, która służy do pracy z plikami.  

```python
plik = open("zaklecia.txt", "r")  # "r" oznacza tryb odczytu
zawartosc = plik.read()       # czytamy całą zawartość pliku
print(zawartosc)
plik.close()                  # zamykamy plik
```

*Otwarcie <-> zamknięcie ... i zawsze trzeba o tym pamiętać! Spokojnie programiści są leniwi i wymyślili lepszy sposób (ale o tym za chwilę)*

## Tryby otwierania pliku

Dlaczego użyłam `r` ?

Parametr **"r"** w `open()` oznacza nic innego niż **tryb odczytu** czyli angielskie read. 
Odczyt jest domyślnym stanem, więc mogliśmy też otworzyć za pomocą `plik = open("zaklecia.txt")`

**Ciekawostka:** Zobacz co zawiera teraz sama zmienna `plik` -> `print(plik)`.


## Słowo kluczowe `with`

Jak wspomniałam programiści są dość leniwi ;) 

Obecnie korzystamy niemal tylko z **`with open(...) as plik:`** – bez ręcznego `close()`. Dzięki temu Python sam pamięta że pliki należy zamykać

```python
with open("zaklecia.txt", "r", encoding="utf-8") as fp:
    zawartosc_zaklecia = fp.read()

print(zawartosc_zaklecia)
```

- `fp` - czyli zmienna, w której będziemy przechowywać obiekt otwartego pliku, równie dobrze możesz nazwać to `p`, `plik`, `my_file` itp 
- `zawartosc_zaklecia` - zmienna, w której odczytana została zawartość pliku jako tekst
- `utf-8` - kodowanie znaków


> TIP
> encoding="utf-8" dodajemy prawie zawsze – zapewnia poprawne wyświetlanie znaków lokalnych, to po prostu dodatkowe zabezpieczenie.
{: .block-tip }

## Odczyt linia po linii 

Czasami chcemy pracować z każdą linią osobno – np. gdy każda linia to inne zaklęcie.

W Pythonie wygodnie zrobimy to funkcją `.readlines()`, która zwraca listę linii:

```python
with open("zaklecia.txt", "r", encoding="utf-8") as fp:
    linie = fp.readlines()  # lista linii z pliku

for zaklecie in linie:
    print(zaklecie.strip())  # strip() usuwa znaki nowej linii - porównaj też kod bez strip()
```

### 🔹 Zadanie 1

`readlines()` daje od razu listę, którą możemy modyfikować, filtrować i przekazywać do innych funkcji - bardzo wygodna sprawa :D

Utwórz plik `domy.txt` zawiera nazwy domów w Hogwarcie (po jednym w każdej linii)

```
Gryffindor

Slytherin

Hufflepuff

Ravenclaw
```

Otwórz plik i:

- odczytaj wszystkie linie do listy,
- wyświetl nazwy domów w formie listy numerowanej
- nie wyświetlaj pustych linii

```
1. Gryffindor
2. Slytherin
3. Hufflepuff
4. Ravenclaw
```

> ##### TIP
>
> Użyj `enumerate()` aby dodać numerowanie do elementów listy.
{: .block-tip }


### 🔹 Zadanie 2


Plik `wpisy.txt` zawiera daty wpisów na listę magicznych wydarzeń (każda data w osobnej linii, np. `1997`, `2003`, `1980`, `1123`, `2021`).  

- Odczytaj plik do listy liczb całkowitych.
- Wyświetl najstarszy i najnowszy rok z pliku.

> ##### TIP
>
> Użyj odpowiednich funkcji do poszukiwania najstarszego i najnowszego roku jako wartości na liście
{: .block-tip }

### 🔹 Zadanie 3

Utwórz plik `wpisy.csv` zawiera wydarzenia magiczne w formacie:

```
Pierwsze Ministerstwo Magii w Monako,1997
Założenie Rady Wewnątrz Magicznej,2003
Utworzenie Gwardii Niewidzialności,1980
Wojny Trolli,1123
Otwarcie herbaciarni Braci Futura w Londynie,2021
```

- Odczytaj plik CSV
- Wyodrębnij daty (druga kolumna)
- Wyświetl najstarszy i najnowszy rok z pliku wraz z nazwami wydarzeń

> ##### TIP
>
> Plik CSV to plik tekstowy ze znakiem podziału. Możesz użyć `.split(",")` aby rozdzielić nazwę wydarzenia i rok.
{: .block-tip }

### 🔹 Zadanie 4

Chcemy odfiltrować dobe i złe zaklęcia.

W pliku `ksiega_zaklec.txt` znajdują się zaklęcia, w tym zakazane 

```
Expelliarmus,zaklęcie rozbrajające
Avada Kedavra,zakazane zaklęcie uśmiercające
Lumos,zaklęcie światła
Nox,zaklęcie gaszenia światła
Crucio,zakazane zaklęcie tortur
Wingardium Leviosa,zaklęcie lewitacji
Alohomora,zaklęcie otwierające
Imperio,zakazane zaklęcie kontroli umysłu
Protego,zaklęcie tarczy
Accio,zaklęcie przywołujące
```

- Zaimportuj moduł `zaklecia` z poprzedniej lekcji (przyda nam się funkcja `filter_spells`).
- Wczytaj całą treść pliku do zmiennej.
- Przefiltruj tekst przez `filter_spells`.
- Wyświetl bezpieczną treść!


## 🛠 Zapis do pliku

Mieliśmy już tryb odczytu, ale to nie koniec.


Inne popularne tryby:

- "w" – zapis (nadpisze istniejący plik), *write*
- "a" – dopisywanie na końcu pliku, *append*
- "r+" – odczyt i zapis.

Czasem chcemy **zapisać coś do pliku** - np. nowe zaklęcia znalezione w bibliotece Hogwartu.
Do tego używamy trybu "w" (write) lub "a" (append).

```python
nowe_zaklecia = [
    "Accio",
    "Lumos",
    "Nox"
]

with open("zaklecia.txt", "a", encoding="utf-8") as fp:
    for z in nowe_zaklecia:
        fp.write(z + "\n")

print("Nowe zaklęcia zostały dopisane do pliku!")
```

**Dlaczego `a` **

Chcesz zachować dotychczasowe dane i dodać nowe, tryb **"w"** skasuje zawartość pliku przed zapisaniem.

#### Przeanalizuj 

```python
import os

nazwa_pliku = input("Podaj nazwę pliku do zapisu - razem z rozszerzeniem!")

# sprawdzamy rozmiar pliku
if os.path.exists(nazwa_pliku) and os.path.getsize(nazwa_pliku) > 0:
    # plik istnieje i nie jest pusty -> tryb append
    with open(nazwa_pliku, "a", encoding="utf-8") as fp:
        fp.write("Nowe zaklęcie: Accio\n")
else:
    # plik nie istnieje lub jest pusty -> tryb write
    with open(nazwa_pliku, "w", encoding="utf-8") as fp:
        fp.write("Pierwsze zaklęcie: Lumos\n")
```


### 🔹 Zadanie 5

- Zaimportuj moduł `random`.
- Wylosuj liczbę od 1 do 100.
- Zapisz do pliku `.txt` (nazwa pliku podana przez użytkownika) tyle znaków `❤︎` ile wynosi wylosowana liczba.


### 🔹 Zadanie 6 

Już wiesz, że plik CSV to w rzeczywistości zwykły plik tekstowy, w którym dane są oddzielone przecinkami.  

- Poproś użytkownika o podanie 3 zaklęć i odpowiadających im efektów.  
- Zapisz te dane do pliku `krotkie_zaklecia.csv` w formacie:  

```
Lumos,Światło
Accio,Przywołanie przedmiotu
Protego,Tarcza ochronna
```

- Pamiętaj o dodaniu nagłówka (pierwsza linia w CSV opisuje kolumny) `Zaklęcie,Efekt`

### 🔹 Zadanie 7 

- Zaimportuj moduł `zaklecia` (funkcja `filter_spells`) z poprzedniej sekcji
- Wczytaj zaklęcia z pliku `ksiega_zaklec.csv`.
- Przefiltruj zaklęcia przez `filter_spells`.
- Zapisz oczyszczone zaklęcia do nowego pliku `bezpieczne_zaklecia.csv`.

### 🔹 Zadanie 8

Stwórz moduł `bezpieczne_pliki.py`, który zajmuje się jedynie **otwieraniem plików** w bezpieczny sposób.

- Funkcja `bezpieczny_odczyt(nazwa_pliku)`:
  - sprawdza czy plik istnieje,
  - sprawdza czy plik nie jest pusty,
  - jeśli plik jest dostępny – odczytuje jego zawartość,
  - jeśli nie – zwraca komunikat o braku danych.

- Funkcja `bezpieczny_zapis(nazwa_pliku, dane)`:
  - sprawdza czy plik już istnieje,
  - jeśli nie – zapisuje dane do nowego pliku
  - jeśli tak – **nie nadpisuje** pliku i zwraca komunikat o konflikcie pyta czy nadpisać plik przed zapisem,


**W pliku `main.py`**:
- zaimportuj moduł `bezpieczne_pliki`,
- przetestuj funkcję odczytu i zapisu na wybranych plikach `.txt` i `.csv`.

