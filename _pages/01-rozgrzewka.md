---
title: 1. Rozgrzewka
layout: post
---

Cześć! 🎈  
Witaj na warsztatach **Python**.  

Masz pytania?  
👾 Link do discorda: [https://discord.gg/Ccm8uG8dGd](https://discord.gg/Ccm8uG8dGd)



Tym razem podstawy Pythona masz już za sobą! 😄  
Znasz pętle, wiesz jak działają funkcje. Teraz przejdziemy do ćwiczeń, które w praktyczny sposób połączą te elementy.  

Dziś wkroczymy w nieco bardziej **meandry programowania** i korzystania z plików i zewnętrznych źródeł danych.  

Na początek — krótka rozgrzewka.

---

## 📜 Zadanie

**Filtr Księgi Zakazanych Zaklęć**. W bibliotece magicznej znajduje się Księga Zaklęć, w której pojawiły się *zakazane formuły*. Trzeba je usunąć, aby księga mogła trafić do uczniów.

### Instrukcja:
1. Napisz funkcję `filter_spells(text, banned)`, która:
   - przyjmuje tekst i listę zakazanych słów (`banned spells`),
   - usuwa zakazane zaklęcia z tekstu ( podpowiedź: ignorując wielkość liter),
   - zwraca nową, bezpieczną wersję tekstu.

2. Stwórz listę kilku fragmentów zaklęć (np. lista stringów).  
3. Użyj dowolnej pętli, aby każdy fragment przefiltrować i wyświetlić oczyszczoną wersję.

```
banned_spells = ["avada",  "imperi", "crucio"]

texts = [
    "Zaklęcie niewybaczaln i śmiertelne to Avada Kedavra",
    "W pojedynku magicznycm Crucio użyte na przeciwniku jest zakazane.",
    "Pamiętaj, ze Alohomora otwiera, choć nie kazde drzwi.",
    "W historii czarodziejów imperializm nie był tak powszechny jak u mugoli.",
]
```
---

🧙‍♂️ **Początek kodu**

```python

def filter_spells(param1, param2):
   ...

# ---- glowna czesc kodu ----

# pętla
...
```