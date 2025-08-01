---
title: 5. CSV i XLS
layout: post
---

Do otwierania specyficznych formatów potrzebne są czasem specyficzne środki.  
Plik `.txt` odczytamy wbudowaną funkcją `open()`, ale pliki **CSV** czy **XLS** wymagają od nas trochę więcej uwagi.

---

## Pliki CSV – co to właściwie jest?

CSV (*Comma Separated Values*) to format danych, w którym kolejne wartości są oddzielone przecinkiem.  
Plik CSV to tak naprawdę zwykły **plik tekstowy** – różni się tylko umową, że przecinki (czasem średniki) oddzielają kolumny.

Przykład `zaklecia.csv`:
```
Zaklęcie,Efekt
Lumos,Światło
Accio,Przywołanie przedmiotu
Protego,Tarcza ochronna
```

## Odczyt CSV w Pythonie

W Pythonie do odczytu CSV możemy użyć zwykłego otwierania lub dedykowanego modułu **`csv`** (wbudowany, nie trzeba instalować).

```python
import csv

with open("zaklecia.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik)
    for wiersz in czytnik:
        print(wiersz)
```

> TIP
> csv.reader() zwraca każdy wiersz jako listę elementów.
> Pierwszy wiersz w pliku to zazwyczaj nagłówki kolumn.
{: .block-tip }

```
['Zaklęcie', 'Efekt']
['Lumos', 'Światło']
['Accio', 'Przywołanie przedmiotu']
['Protego', 'Tarcza ochronna']
```

## Zapis CSV w Pythonie
Zapiszmy listę zaklęć i efektów do pliku CSV  ✍️

```python
import csv

zaklecia = [
    ["Zaklęcie", "Efekt"],
    ["Lumos", "Światło"],
    ["Accio", "Przywołanie przedmiotu"],
    ["Protego", "Tarcza ochronna"]
]

with open("zaklecia_nowe.csv", "w", encoding="utf-8", newline="") as plik:
    zapis = csv.writer(plik)
    zapis.writerows(zaklecia)
    print('✔ Zapisano!')
```

## 📊 Pliki XLS – Ah, ten Excel!

Operowanie na plikach xls nie jest łatwym zadaniem, ale oczywiście są do tego gotowe narzędzia. 

Pliki XLS/XLSX (Excel) już nie jest zwykły tekst, ale całkiem sporo dodatków wokół danych narzuca nam sam ten program, dlatego do ich odczytu i zapisu potrzebujemy biblioteki, np.:

- `openpyxl` – do plików `.xlsx`
- `xlrd` – do odczytu starych `.xls`
-  ale też`pandas` - wygodny sposób do analizy danych

Doinstalujmy biblioteki, które nam się przydadzą w dalszej części (możemy je wymienić po spacji).

```bash
pip install pandas openpyxl matplotlib
```

Utwórz dowolny plik `zaklecia.xlsx` (nie masz MS Excel? - Google Spreadsheets z zapisem do XLSX)

```python
from openpyxl import load_workbook

wb = load_workbook("zaklecia.xlsx")
arkusz = wb.active

for wiersz in arkusz.iter_rows(values_only=True):
    print(wiersz)
```

Możliwy jest też zapis!

```python
from openpyxl import Workbook

wb = Workbook()
arkusz = wb.active

arkusz.append(["Zaklęcie", "Efekt"])
arkusz.append(["Lumos", "Światło"])
arkusz.append(["Accio", "Przywołanie przedmiotu"])

wb.save("zaklecia.xlsx")
```

> TIP
> pandas jest świetny do szybkiej analizy danych w Excelu (filtry, grupowanie, statystyki) i w większości projektów zastępuje bezpośrednie użycie openpyxl w analizie.
{: .block-tip }

### Pandas?

![]({{ site.baseurl }}/assets/pandas.gif)


`pandas` to bardzo popularna biblioteka do pracy z danymi tabelarycznymi.  
Potrafi odczytać i zapisać pliki **XLSX** w kilka linijek kodu.

Aby `pandas` mógł pracować z plikami Excela, potrzebny jest też silnik `openpyxl`, gdyż pandas używa go podspodem.


#### Jak odczytać dane za pomocą pandas? 

```python
import pandas as pd

# odczyt pliku XLSX do DataFrame
df = pd.read_excel("zaklecia.xlsx")

print(df)
```

```
  Zaklęcie          Efekt
0   Lumos         Światło
1   Accio   Przywołanie
2  Protego  Tarcza ochronna
```

**Zapis?  Ależ proszę!**
```python
# dodanie nowego wiersza
nowy_wiersz = {"Zaklęcie": "Expelliarmus", "Efekt": "Rozbrojenie"}
df = df._append(nowy_wiersz, ignore_index=True)

# zapis do nowego pliku
df.to_excel("nowe_zaklecia.xlsx", index=False)
```

> TIP
> pandas automatycznie rozpoznaje nagłówki w pierwszym wierszu pliku XLSX.
> Przy zapisie ustaw `index=False`, aby nie dodawać kolumny indeksów.
{: .block-tip }


### Zadanie - MINIPROJEKT ✨🪄

![]({{ site.baseurl }}/assets/abrakadabra.gif)

**Uwaga: 🤝 Łączymy się w pary lub trójki!**  

🚫🤖 *Używamy głowy i dokumentacji, unikaj używania AI*

Stwórz program, który analizuje dane z pliku CSV i generuje raport.  
Na potrzeby ćwiczenia możemy skorzystać z pliku `zaklecia_statystyki.csv` (przykładowy plik poniżej).

🎯 **Zakres**

1. **`analiza_zaklec.py`**
   - Utwórz moduł zawierający funkcje:
     - `wczytaj_dane()` – wczytuje dane z pliku CSV.
     - `statystyki_podstawowe()` – liczy łączną liczbę użyć zaklęć, znajduje najczęściej używane zaklęcie, zlicza zaklęcia zakazane.
     - `statystyki_typow()` – liczy średnią liczbę użyć dla każdego typu i typ z największą sumaryczną liczbą użyć.
     - *(Opcjonalnie)* `zapisz_raport()` – zapisuje wyniki do pliku CSV lub XLSX.


> ##### 💡 TIP
>
> Poznaj możliwości pandas'a. To biblioteka idealna do wielu zadań statystycznych.
> Do obliczeń w `pandas` przyda się `groupby()` z `mean()` lub `sum()` oraz `max()` do wyszukania wartości największej.
{: .block-tip }

{% include bookmark.html 
    url="https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html"
    title="Pandas – Intro Tutorials"
    desc="Oficjalne wprowadzenie do biblioteki Pandas: samouczki dla początkujących"
%}

2. **Plik główny projektu np. `main.py`**
   - Zaimportuj moduł `analiza_zaklec`.
   - Wczytaj dane z pliku `zaklecia_statystyki.csv`.
   - Wyświetl w konsoli raport wygenerowany przez funkcje modułu.
   
3. **Format raportu w konsoli**
   - Wyświetl w konsoli raport w formacie:
     ```
     Łączna liczba użyć zaklęć: X
     Najczęściej używane zaklęcie: Y (Z użyć)
     Liczba zaklęć zakazanych: Z

     
     Średnia liczba użyć według typu:
     -Światło: ...
     -Obrona: ...
     -...
     Typ z największą liczbą użyć: ...
     ```

4. **(Opcjonalnie)** Zapis raportu do pliku `raport.csv` i / lub `raport.xslx`

> ##### 💡 TIP
>
> Plik CSV musi mieć nagłówki w pierwszym wierszu (np. `Zaklęcie,Typ,Użycia`).  
> Upewnij się, że zapisujesz plik w kodowaniu **UTF‑8**, aby poprawnie wyświetlały się polskie znaki.
{: .block-tip }



Skopiuj plik `zaklecia_statystyki.csv`
```
Zaklęcie,Typ,Użycia
Lumos,Światło,150
Nox,Światło,85
Accio,Przywołanie,92
Wingardium Leviosa,Lewitacja,73
Protego,Obrona,120
Protego Maxima,Obrona,45
Expelliarmus,Atak,180
Rictusempra,Atak,40
Stupefy,Atak,98
Avada Kedavra,Zakazane,0
Crucio,Zakazane,0
Imperio,Zakazane,0
Alohomora,Otwieranie,61
Colloportus,Otwieranie,34
Revelio,Odkrywanie,56
Homenum Revelio,Odkrywanie,28
Expecto Patronum,Obrona,142
Petrificus Totalus,Atak,77
Rennervate,Leczenie,39
Episkey,Leczenie,48
Ferula,Leczenie,20
Obliviate,Pamięć,15
Legilimens,Pamięć,19
Morsmordre,Zakazane,0
Sectumsempra,Zakazane,0
Silencio,Kontrola,33
Tarantallegra,Kontrola,25
Engorgio,Transformacja,51
Reducio,Transformacja,47
Incendio,Ogień,59
Aguamenti,Woda,37
```


### Za mało emocji? Przygotuj diagramy (Opcjonalnie)
Dla wcześniej zebranych danych wyświetl


> ##### 💡 TIP
>
> W `pandas` możesz łatwo stworzyć wykres przy pomocy `.plot(kind='name')` np. `.plot(kind='pie')`.  
> Aby zapisać wykres do pliku, użyj `plt.savefig("wykres.png")`.
{: .block-tip }


Zobacz przykład użycia 

```python
import pandas as pd


zwierzeta = ["Kot", "Sowa", "Ropucha", "Szczur"]
glosy     = [23, 15, 8, 3]

# DataFrame z dwóch list
df = pd.DataFrame({"Zwierzę": zwierzeta, "Głosy": glosy})

# wykres słupkowy
df.plot(x="Zwierzę",
        y="Głosy",
        kind="bar",
        title="Ulubione zwierzęta wśród uczniów")
```

#### 1️⃣ **Wykres słupkowy – suma użyć według typu**
- Pokazuje, które typy zaklęć są używane najczęściej. Przyda się w raporcie do pokazania dominujących kategorii.
- Oś X: typ zaklęcia
- Oś Y: suma użyć

#### 2️⃣ **Wykres kołowy - udział typów w łącznej liczbie użyć**

Jaki procent wszystkich użyć to np. „Światło” vs „Obrona” itd.

#### 3️⃣ **Top 5 zaklęć - wykres słupkowy**
Najczęściej używane konkretne zaklęcia (nie typy).
- Oś X: nazwy zaklęć (top 5 po liczbie użyć)
- Oś Y: liczba użyć

---

Hip hip hurra, czas na list z Hogwartu! 👉