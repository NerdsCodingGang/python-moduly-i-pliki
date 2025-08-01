---
title: 2. Moduły i biblioteki standardowe
layout: post
---

W tej lekcji przechodzimy do bardzo ważnej części Pythona – **modułów i bibliotek**.  
Do tej pory pisaliśmy wszystko samodzielnie. Jednak wiele przydatnych funkcji jest już **gotowych** i czeka na użycie. Python ma ogromny zestaw gotowych narzędzi, które możesz wykorzystać w swoim kodzie.
Mozliwe, ze znasz juz modul `random` albo `math`, ale czym one tak naprawde są? 

---

## 🔍 Co to jest moduł a czym biblioteka?

- **Moduł**: plik `.py`, który zawiera kod Pythona – funkcje, zmienne, klasy mozemy je reuzyć.  
- **Biblioteka**: zbiór modułów (często instalowany razem z Pythonem lub dodatkowo).  
- **Biblioteka standardowa**: zestaw modułów, które są dostępne w Pythonie od razu, bez instalowania.

```python
import nazwa_modułu
```

### 🔹 Zadanie 1
1. Zaimportuj moduł random i wylosuj liczbę od 1 do 100, a następnie wyświetl tyle `❤︎` co wylosowana liczba.

2. Zaimportuj moduł math i znajdź logarymt naturalny, kwadratowy i logarytm dziesiętny z liczby 256,

### 🔹 Zadanie 2
Zaimportuj moduł datetime i wyświetl dzisiejszą datę
    Wyświetl datę w kilku formatach, np.:

    - `YYYY-MM-DD` (np. 2025-07-29)
    - `DD.MM.YYYY` (np. 29.07.2025)
    - Dzień tygodnia, DD Miesiąc YYYY (np.`Tuesday, 29 July 2025`)
    - Format ISO (`2025-07-29T14:30:00`)

{% include bookmark.html 
    url="https://www.flynerd.pl/2022/09/python-datetime-podstawy.html"
    title="Poznaj moduł datetime"
    desc="👉 Podstawy modułu datetime w Pythonie"
%}

### 🔹 Zadanie 3

Korzystaliśmy z bibliotek dostępnych w Pythonie, ale możemy też coś doinstalować.

Do kolejnego zadania musisz skorzystać z managera pakietów Pythona, aby zainstalować zewnętrzną bibliotekę. W konsoli (terminalu, wierszu poleceń) wykonaj wklej poniższą komendę i naciśnij enter

```
pip install requests 
```

Uwaga  jeśli używasz komendy `python3` to również użyj `pip3` do instalacji.


Następnie wykorzystaj poniższy fragment kodu, aby wykonać zadanie

```python
import requests #skorzystaj z pakietu request

req = requests.get("http://numbersapi.com/random/year") # odpytujemy API, zewnętrzne źródło danych
print(req.text)

```

- Sprawdź czy pobrany tekst ze strony zawiera liczbę "13"
- Zapytaj użytkownika o dowolny ciąg znaków.
- Sprawdź czy tekst ze strony zawiera też ciąg zadany przez użytkownika


### 🔹 Zadanie 4 - pogodynka 🌤
Strona OpenWeatherMap udostępnia różnego rodzaju informacje o pogodzie. Skorzystaj z dokumentacji [Current Weather](https://openweathermap.org/current). Przyjrzyj się jak zbudowany jest adres URL. 

Pozwól użytkownikowi podać miasto oraz dwuliterowy kod kraju. Możesz ograniczyć miasta przez wybór kraju w prostym menu np.

- United Kingdom - uk
- Poland - pl
- Germany - de
- itd...

Pokaż użytkownikowi krótkie zdanie o pogodzie oraz temperaturę w st. Celsjusza.

*Uwaga: OpenWeather API może wymagać autoryzacji. Należy założyć darmowe konto i w miejsce appid podać swój klucz konta (`&APPID=your_key`)*


