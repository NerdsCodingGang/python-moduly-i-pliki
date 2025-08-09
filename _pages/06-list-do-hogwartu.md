---
title: 6.🔮 Email z Hogwartu ✨
layout: post
---

Do tego zadania przyda się więcej niż 1 głowa, współpracujcie razem aż do skutku 
Na razie nasze programy tylko czytały i zapisywały pliki. Czas na kolejny poziom magiczny czyli automatyczne wysyłanie maili!


W tym zadaniu:
- skonfigurujesz bezpieczne logowanie SMTP,
- wyślesz pierwszy e-mail „do siebie”,
- wyślesz spersonalizowane zaproszenia do Hogwartu!


## Utwórz skrzynkę testową Gmail

Załóż nową skrzynkę Gmail do ćwiczeń (np. `testingmagic123456@gmail.com`).

> ##### OSTRZEŻENIE
>
> Nie używaj głównego konta czy jego hasła do Gmaila w kodzie!
{: .block-danger }


**Dlaczego nowa skrzynka?**
- Będziemy generować hasło do aplikacji – lepiej nie robić tego na prywatnym koncie.
- Unikamy wysyłania maili testowych przez korzystanie z waszej głównej skrzynki, w przypadku zablokowania przez Google.

**3 kroki:**

1. Włącz weryfikację dwuetapową (2FA) w ustawieniach Google.
2. Otwórz Hasła aplikacji (np. „MyPythonApp”).
3. Zapisz wygenerowane 16-znakowe hasło — będzie Twoim kluczem SMTP.


### Ustawienia konta Google zakładka bezpieczeństwo (security)

Włączamy **weryfikację 2-etapową** (najszybciej za pomocą nr telefonu)
![]({{ site.baseurl }}/assets/2fa_1.png)


### Otwórz hasło aplikacji

Wyszukaj "hasła aplikacji" / "app paswords"

![]({{ site.baseurl }}/assets/2fa_2.png)

 → Aplikacja wpisujemy wybraną nazwę (np. „MyPythonApp”)

![]({{ site.baseurl }}/assets/2fa_3.png)

→ **Zatwierdź** "utwórz" / "create"

### Uzyskanie klucza 

![]({{ site.baseurl }}/assets/16key.png)

Zapisz go, będzie Ci potrzebny, to Twój prywatny, sekretny klucz  🗝️
 → Strzeż go dobrze!

## Przygotuj środowisko Pythona 🐍


- potrzebne nam jeszcze moduły `smtplib` i `email`, ale masz już w standardowej bibliotece Pythona

Zbierz potrzebne dane

```bash
MAIL_USER=testing_magic_13454353@gmail.com
MAIL_PASSWORD=tu_wklej_16znakowy_klucz
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
```

> ##### **DLA CIEKAWYCH** 👀
>
> 📬 * Co to jest host SMTP?*
> - **Host SMTP** to **adres serwera pocztowego**, który “odbiera” od nas wiadomości i wysyła je dalej.  
> - To tak jak **adres biura pocztowego**:  
>   - Gmail: `smtp.gmail.com`  
>   - Outlook: `smtp.office365.com`  
>   - Onet: `smtp.poczta.onet.pl`  
> - Program (np. Python) musi wiedzieć, **gdzie wysłać nasz e-mail**, więc podajemy adres hosta.
>
>
> 🔌 *Co to jest port?*
> - **Port** to **numer “drzwi” w tym biurze pocztowym**, przez które program ma się połączyć.  
> - Serwer poczty ma wiele “drzwi” (portów), ale dla wysyłki e-mail najczęściej używa się:  
>   - `465` — połączenie **bezpieczne (SSL)**  
>   - `587` — połączenie **bezpieczne (TLS)**  
> - To trochę jak numer okienka w urzędzie: port mówi, **którym wejściem wchodzimy**.
>
> ---
>
> 📌 Przykład (dla Gmaila)
> - **Host SMTP:** `smtp.gmail.com`  
> - **Port:** `465` (SSL) lub `587` (TLS)  

--- 

Zebrane dane możesz już uzupełnić bezpośrednio w swoim pliku np. `wysylka_email.py` 


> ##### OSTRZEŻENIE
>
> **Nie nazywaj pliku:** `email.py`
> Tak nazywa się już moduł w pythonie, którego używasz. 
> Impotujemy z modułu `email` obiekt `message` - patrz poniżej.
{: .block-danger }


Plik: `wysylka_email.py`: 

```python
import smtplib
from email.message import EmailMessage

#  KONFIGURACJA – UZUPEŁNIJ SAMODZIELNIE
MAIL_USER = "testingmagic13454353@gmail.com"   # ← twój adres
MAIL_PASSWORD = "ab12cd34ef56gh78"             # ← 16-znakowy klucz aplikacji
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL

```

## Wyślij pierwszy mail do siebie ✉️

Wyślij na własną skrzynkę testową wiadomość:

- Temat: My magical me
- Treść: Tak magiczny email, że oczarował nawet mnie!

### 🤔 Co trzeba zrobić?

- Utwórz obiekt wiadomości (`EmailMessage`).
- Ustaw `subject`, `from`, `to`, `set_content(...)`.
- Połącz się z serwerem SMTP (`smtplib.SMTP_SSL`).
- Wyślij maila (`smtp.send_message(msg)`).
- Zamknij połączenie i sprawdź skrzynkę  
  *(lub użyj `with`, wtedy sesja zamknie się automatycznie)*.


### Podpowiedzi - krok po kroku

Utwórz obiek wiadomości, poszukaj jakie możliwości Ci daje  `EmailMessage()`

```python
msg = EmailMessage()
```

{% include bookmark.html
   url="https://docs.python.org/3/library/email.examples.html"
   title="Przykłady modułu email – oficjalna dokumentacja"
   desc="Receptury biblioteki email" %}


**Wysyłanie**

```python
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp_setup:
    smtp_setup.login(MAIL_USER, MAIL_PASSWORD)
    smtp_setup.send_message(msg)

print("✅ Mail wysłany — sprawdź skrzynkę (lub folder Spam).")

```

| Linia | Co się dzieje? | Dlaczego tak? | Gdzie szukać więcej |
|-------|---------------|---------------|---------------------|
| `with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as zmienna:` | nawiązujemy **szyfrowane połączenie SSL/TLS** z serwerem SMTP; blok `with` gwarantuje automatyczne zamknięcie sesji | Gmail wymaga szyfrowania: SSL (port 465) lub STARTTLS (port 587) | *python smtplib SSL example*<br>*SMTP Objects* w dokumentacji `smtplib` |
| `smtp.login(MAIL_USER, MAIL_PASSWORD)` | logujemy się adresem e-mail i **16-znakowym hasłem aplikacji** | Gmail w SMTP akceptuje wyłącznie hasła aplikacji (2FA włączone) | *gmail app password SMTP*<br>Google Help „Sign in using App Passwords” |
| `smtp.send_message(msg)` | wysyłamy obiekt `EmailMessage` na adres z pola **To** | `send_message()` sam konwertuje wiadomość do formatu MIME i wysyła | [Przykłady modułu `email`](https://docs.python.org/3/library/email.examples.html) |



> ##### Błąd?
>
> Jeśli zobaczysz błąd smtplib.SMTPAuthenticationError, upewnij się, że:
> - używasz klucza aplikacji, a nie zwykłego hasła,
> - konto ma włączone 2-etapowe logowanie,
> - podajesz poprawny port (465) i wykorzystujesz SMTP_SSL.
{: .block-danger }


{% include solution.html title="Kliknij tu w ostateczności (rozwiązanie)" content="
<pre><code class='language-python'>
from email.message import EmailMessage
import smtplib

SMTP_HOST = 'smtp.example.com'
SMTP_PORT = 465
MAIL_USER = 'twojemail@example.com'
MAIL_PASSWORD = 'twoj-sekretny-klucz'

msg = EmailMessage()
msg['Subject'] = 'My magical me'
msg['From'] = MAIL_USER
msg['To'] = MAIL_USER
msg.set_content('Tak magiczny email, że oczarował nawet mnie!')

with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp_setup:
    smtp_setup.login(MAIL_USER, MAIL_PASSWORD)
    smtp_setup.send_message(msg)

print('✅ Mail wysłany — sprawdź skrzynkę (lub folder Spam).')
</code></pre>
" %}


---

## List z Hogwartu ✉️

Przygotuj listę osób z Twojego stolika (email może Ci podadzą a może nie - nie zmuszamy, można też podać nasze nowo wygenerowane fałszywe maile)

np. `stolik.csv`

```
Imię,Email
Harry,harry@example.com
Hermiona,hermiona@example.com
Ron,ron@example.com
```

Utwórz też plik `txt` z szablonem wiadomosci. `{imie}` to placeholder — Twój program zastąpi go prawdziwym imieniem.

```
Drogi {imie},

Z przyjemnością informujemy, że zostałeś przyjęty do Hogwartu!
Twój list czeka na Ciebie w sowiarni.

Z magicznymi pozdrowieniami,
Dyrekcja Hogwartu
```

### 🤔 Co trzeba zrobić?

- Odczytaj `stolik.csv` — użyj dowolnej poznanej metody.  
- Dla każdej osoby:  
  - wczytaj treść `szablon.txt`,  
  - podmień `{imie}` na imię z pliku,  
  - utwórz wiadomość (`EmailMessage`),  
  - ustaw temat, nadawcę, odbiorcę, treść,  
  - wyślij przez SMTP.  

Po wysyłce wypisz w konsoli np. `Wysłano do: Harry <harry@example.com>`.

#### REFAKTOR

Przepisać rozwiązanie tak, by uzywać wszystkiego co do tej pory umiemy na przykład:

- kod był podzielony na funkcje o nazwach mówiących, co robią (czasowniki: `read_people`, `read/render_template`, `build_email`, `main`),
- warto podzielić kod na moduły (wprowadź chociaż 1 moduł np. czytanie pliku - reuzyjesz go dla ludzi jak i czytania szablonu)
- pamiętaj by użyć `if __name__ == "__main__":` do uruchamiania programu
- walidacja e‑maila jeśli email nie zawiera @, oznacz rekord jako „do poprawy” i pomiń go w wysyłce

### Rozszerzenie 

- spersonalizuj emaile **Temat: List z Hogwartu dla {imie}**
- przy wczytywaniu CSV przytnij spacje (`strip()`), ujednolić imiona (`title()`), puste e‑maile zamień na `brak emaila` i wyświetl w konsoli, że dla tego użytkownika zabrakło nam danych i nie da się mu wysłać maila! 
- na koniec wypisz: `Wysłano: X, Pominięto: Y`. np. `Wysłano 12, Pominięto 2 emaile`
-  pozwól użytkownikowi wybrać, ilu pierwszych odbiorców wysłać (np. „wyślij tylko 3 pierwsze”)

#### Książki szkolne

Utwórz nowy plik z listą książek 

```
Księga Standardowych Zaklęć (1 stopień) - Miranda Goshawk
Historia Magii - Bathilda Bagshot
Teoria Magii - Adalbert Waffling
Wprowadzenie do Transmutacji - Emeric Switch
Tysiąc Magicznych Roślin i Grzybów - Phyllida Spore
Magiczne Eliksiry i Napoje - Arsenius Jigger
```

W mailu do studentów wyślij numerowaną listę książek, jakie muszą nabyć przed początkiem roku akademickiego na ulicy.


> ##### **TIP**
>
> W pętli `for` przypomnisz sobie `enumerate()` lub klasyczne iterowanie list.
{: .block-tip }


#### Wróżba na dzisiaj

Użyj darmowego API `https://horoscope-app-api.vercel.app/` by wygenerować magiczną wróżbę, którą wyślesz emailem dla swoich uczniów.


👉  Niedosyt? Pomyśl co możesz zrobić z dzisiaj nabytą wiedzą!

👉  Napisz własne pomysły na rozszerzenia i podziel się ze swoim stolikiem