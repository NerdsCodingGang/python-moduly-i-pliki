---
title: 3. Tworzymy moduły
layout: post
---

Do tej pory korzystaliśmy z **modułów wbudowanych** w Pythona (`math`, `random`, `datetime`).  
Teraz zrobimy **własny moduł** – tak samo jak robią to twórcy bibliotek.  
Będziemy mogli go importować i używać w innych plikach.


** 📂 Nasz pierwszy własny moduł – BMI**

Zaczniemy od prostego programu liczącego **BMI** na podstawie wzrostu i wagi.

---

Załózmy, ze chcemy obliczć BMI, wzór znany nam dobrze z czasów szkolnych.

$$
BMI = \frac{\text{masa ciała (kg)}}{\text{wzrost (m)}^2}
$$


Stwórz plik **skrypt.py** i wpisz:

```python
waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

bmi = waga / (wzrost ** 2)
print("Twoje BMI wynosi:", bmi)
```

Ten kod działa, ale:

- jeśli chcemy policzyć BMI w innym projekcie, musimy go **kopiować**,
- jeśli chcemy go przetestować bez wprowadzania danych za każdym razem, jest to **niewygodne**.

To jest moment, w którym przenosimy logikę do modułu.

## Zamykamy logikę w funkcji
Funkcja pozwala nam policzyć BMI dla dowolnych danych wejściowych – bez pytania użytkownika.

```python
def oblicz_bmi(waga, wzrost):
    return waga / (wzrost ** 2)

waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

print("Twoje BMI wynosi:", oblicz_bmi(waga, wzrost))
```


## A po co `if __name__ == "__main__"` ?

W plikach Pythonowych, w programach zawodowych programistów pojawia się tajemnicze `__name__`. Jest to specjalna zmienna Pythona, która "wie", gdzie się znajduje właśnie wykonywany program. 


- Jeśli plik uruchamiany jest bezpośrednio – `__name__` ma wartość `"__main__"`.
- Jeśli plik jest importowany jako moduł – `__name__` ma wartość `nazwa pliku`.

Dzięki temu możemy rozdzielić:

- kod, który ma się wykonać przy uruchomieniu po prostu pliku,
- a kod, który ma być dostępny tylko po imporcie modułu w pliku

#### Nie wierzysz? Sprawdź to 

Utwórz plik: `modul_testowy.py`

```python
print("Kod w modul_testowy.py został uruchomiony")
print("Wartość __name__ w modul_testowy.py to:", __name__)

def powiedz_czesc():
    return "Cześć z modułu!"
```


Utwórz plik główny np. `main.py` w tym samym folderze co moduł testowy

```python
import modul_testowy

print("Kod w main.py został uruchomiony")
print("Wartość __name__ w main.py to:", __name__)

# wywołanie funkcji z modułu
print(modul_testowy.powiedz_czesc())
```

**A jak to uruchomić i co zobaczymy?**

Gdy uruchomimy plik modułu, czy przez VSC czy komendą `python modul_testowy.py`

efekt:

```
Kod w modul_testowy.py został uruchomiony
Wartość __name__ w modul_testowy.py to: __main__

```

Dziwne? Niekoniecznie!

✅ Tu widać, że zmienna `__name__` przechowuje tekst  `__main__`, bo plik uruchamiany jest bezpośrednio.


Ale, gdy uruchomimy główny plik, który korzysta z modułu `modul_testowy.py` czyli importuje `import modul_testowy` wynik jest juz trochę inny:

```
Kod w modul_testowy.py został uruchomiony
Wartość __name__ w modul_testowy.py to: modul_testowy
Kod w main.py został uruchomiony
Wartość __name__ w main.py to: __main__
Cześć z modułu!
```

✅ Tu widać, że:
- przy imporcie modułu `modul_testowy`, jego `__name__ = modul_testowy`,
- plik `main.py`, uruchomiony bezpośrednio, ma `__name__ = __main__`.


## Rozwijamy skrypt BMI 
Poprawmy nasz plik `skrypt.py` liczący BMI :

```python
def oblicz_bmi(waga, wzrost):
    return waga / (wzrost ** 2)

if __name__ == "__main__": # to się uruchomi zaraz po uruchomieniu skryptu
    waga = float(input("Podaj swoją wagę (kg): "))
    wzrost = float(input("Podaj swój wzrost (m): "))
    print("Twoje BMI wynosi:", oblicz_bmi(waga, wzrost))
```

Teraz kiedy uruchomimy plik `skrypt.py` kod  wewnątrz ifa wykona się od razu.  

## 📂 Tworzymy własny moduł

Stwórz nowy plik bmi.py.

Przenieś tam funkcję `oblicz_bmi`:

```python
def oblicz_bmi(waga, wzrost):
    wynik = waga / (wzrost ** 2)
    return wynik
```

Słowo kluczowe `return` zwraca wartość wyniku, który obliczyliśmy.

## 📥 Import modułu w głównym pliku
W pliku `skrypt.py` możemy teraz zaimportować nasz moduł:

```python
import bmi

if __name__ == "__main__":
    w = float(input("Podaj swoją wagę (kg): "))
    h = float(input("Podaj swój wzrost (m): "))
    bmi_uzytkonika = bmi.oblicz_bmi(w, h)
    print("Twoje BMI wynosi:", round(bmi_uzytkonika, 2))
```

Brawo! 🎉 Właśnie stworzyliśmy i użyliśmy pierwszy własny moduł.

Czas na trening

## ZADANIA

### 🔹 Zadanie 1

Stwórz moduł `zaklecia.py z` funkcją przywitaj(imie), która wyświetla komunikat:
```
Witaj, {imie}! Twoja przygoda w Hogwarcie się zaczyna!
W pliku głównym (np. `zadanie_1.py`) zaimportuj moduł i przywitaj wybraną postać.
```

### 🔹 Zadanie 2
W lekcji rozgrzewkowej stworzyliśmy funkcję `filter_spells`, która oczyszcza tekst z zakazanych zaklęć.
Czas przenieść ją do osobnego modułu by użyć w innych plikach.

Możesz wykorzystać istniejący moduł `zaklecia.py` i przenieś do niego funkcję `filter_spells`.
W pliku głównym `zadanie_2.py`:
- zaimportuj moduł `zaklecia`,
- utwórz listę przykładowych zdań `texts`
- wywołaj `filter_spells` dla przykładowych tekstów z listy,
- wyświetl wyniki filtrowania po usunięciu zakazanych słów

### 🔹 Zadanie 3 
Moduł liczący punkty dla domu 🏆

Stwórz moduł **`punkty.py`** z funkcjami:

```python
def dodaj_punkty(dom, liczba_punktow):
    ...

def odejmij_punkty(dom, liczba_punktow):
    ...
```

Zaimportuj go w pliku głównym `zadanie_3.py` i użyj.

Wyświetli komunikat:

```bash
Dom Gryffindor otrzymuje 10 punktów!
Dom Slytherin traci 5 punktów!
```

### 🔹 Zadanie 4

Moduł „Sklep w Hogsmeade”

Stwórz moduł **sklep.py**:

- Utwórz zmienną `magazyn` - najlepiej słownik (np. poszukaj w Google jak wygląda słownik w Pythonie) nazwa produktu → cena

```python
magazyn = {
    "Czekoladowa żaba": 10,
    "Maślane piwo": 7,
    "Pióro feniksa": 50
 }

 print(magazyn["Czekoladowa żaba"])
```

- Napisz funkcję `kup(produkt, galeony)`, która:
  - sprawdza, czy produkt jest dostępny w `magazynie`,
  - jeśli tak i użytkownik ma wystarczającą liczbę galeonów – zwraca komunikat:  
    `Kupiłeś <produkt>! Zostało Ci <kwota> galeonów.`,
  - jeśli nie – zwraca komunikat:  
    `Nie stać Cię na <produkt>!`
  - jeśli produkt nie istnieje – zwraca komunikat:  
    `Taki produkt nie istnieje w sklepie.`

Funkcja `kup(produkt, galeony)` może od razy wyświetlać, albo faktycznie coś zwracać za pomocą słowa kluczowego `return`.

W pliku **`zadanie_4.py`**:
- zaimportuj moduł `sklep`,
- przetestuj zakupy kilku produktów (np. „Czekoladowa żaba”, „Maślane piwo”).

👉  Rozszerzenie
Funkcja `kup()` to tylko komunikat — nie modyfikuje stanu magazynu. Jako dodatkowe zadanie: usuń produkt po zakupie.


### 🔹 Zadanie 5 

Wykorzystamy **API Narodowego Instytutu Dziedzictwa**:  
[https://api.zabytek.gov.pl/nidrestapi/api/data/geoportal/otwarteDaneZestawienieUn?format=json](https://api.zabytek.gov.pl/nidrestapi/api/data/geoportal/otwarteDaneZestawienieUn?format=json)

Dane zawierają listę zabytków UNESCO w Polsce w formacie JSON (np. `nazwa`, `wojewodztwo`, `miejscowosc`, `dataWpisu`).

![]({{ site.baseurl }}/assets/malbork.jpg)



**Utwórz moduł `unesco.py`** z funkcją:
    - `pobierz_dane()` – pobiera dane z API (requests) i zwraca listę zabytków.

Upewnij się w pliku głównym, że jesteś w stanie wyświetlić dane.



---

#### Filtrowanie po dacie 📅

Do modułu dodaj funkcję `znajdz_nowsze(dane, rok)` – zwraca listę zabytków wpisanych na listę UNESCO **po podanym roku**.

**W pliku `main.py`**:
   - pobierz dane z API przy pomocy funkcji `pobierz_dane()`,
   - zapytaj użytkownika o rok (np. 2000),
   - wyświetl zabytki wpisane po tej dacie wraz z rokiem wpisu
   - jeśli nie ma takich zabytków, wyświetli komunikat `"Nie znaleziono zabytków UNESCO wpisanych po roku <rok>"`

Dla chętnych: *Dodaj też opcję szukania starszych niż podana data*

---

#### Filtrowanie po województwie 🗺️

Dodaj w module `unesco.py` nową funkcję:
   - `filtruj_po_wojewodztwie(dane, wojewodztwo)` – zwraca listę zabytków z wybranego województwa.

 **W pliku `main.py`**:
   - zapytaj użytkownika o województwo,
   - przefiltruj dane po województwie,
   - wyświetl wyniki (nazwa, miejscowość, rok wpisu), obsłuż też brak wyniku


Podpowiedź:

Plik `unesco.py`

```python

import requests

API_URL = "https://api.zabytek.gov.pl/nidrestapi/api/data/geoportal/otwarteDaneZestawienieUn?format=json"

def pobierz_dane():
    """pobiera dane z API i zwraca listę zabytków"""
    lista_zabytkow = ...
    return lista_zabytkow

def znajdz_nowsze(dane, rok):
    """zwraca zabytki wpisane po podanym roku"""
    wynik = []
    return wynik

def znajdz_starsze(dane, rok):
    """opcjonalnie: zwraca zabytki wpisane przed podanym rokiem"""
    wynik = []
    return wynik

def filtruj_po_wojewodztwie(dane, wojewodztwo):
    """zwraca zabytki z wybranego województwa"""
    wynik = []
    return wynik
```

Plik `unesco.py`

```python

import unesco

if __name__ == "__main__":
    # pobierz dane
    dane = unesco.pobierz_dane()
    print("Pobrano dane o zabytkach UNESCO.")

    # zapytaj o rok

    # filtrowanie po dacie
    nowsze = ...

    # czy znaleziono dane? / czy lista wynikow pusta
    # ---> lista pusta => komunikat brak wyników
    # ---> lista niepusta => w pętli wyświtl : nazwa zabytku - data wpisania: rok - miejscowość , wojewodztwo
    
    # filtrowanie po województwie
    # +analogicznie wczesniejszego
```