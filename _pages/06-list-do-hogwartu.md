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

> **OSTRZEŻENIE**
>
> Nie używaj głównego konta czy jego hasła do Gmaila w kodzie!
{: .block-warning }


**Dlaczego nowa skrzynka?**
- Będziemy generować hasło do aplikacji – lepiej nie robić tego na prywatnym koncie.
- Unikamy wysyłania maili testowych przez korzystanie z waszej głównej skrzynki, w przypadku zablokowania przez Google.


1. Włącz weryfikację dwuetapową (2FA) w ustawieniach Google.
2. Otwórz Hasła aplikacji → wybierz Poczta → Inne (np. „PythonApp”).
3. Zapisz wygenerowane 16-znakowe hasło — będzie Twoim kluczem SMTP.


## Przygotuj środowisko Pythona 🐍


- potrzebne nam jeszcze moduły `smtplib` i `email` masz już w standardowej bibliotece Pythona

Zbierz potrzebne dane

```bash
MAIL_USER=testing_magic_13454353@gmail.com
MAIL_PASSWORD=tu_wklej_16znakowy_klucz
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
```

Możesz już je uzupełnić w swoim pliku w pythonie

```python

import smtplib
from email.message import EmailMessage

#  KONFIGURACJA – UZUPEŁNIJ SAMODZIELNIE
MAIL_USER = "testing_magic_13454353@gmail.com"   # ← twój adres
MAIL_PASSWORD = "ab12cd34ef56gh78"               # ← 16-znakowy klucz aplikacji
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL

```

## Wyślij pierwszy mail do siebie ✉️

Wyślij na własną skrzynkę testową wiadomość:

- Temat: My magical ME
- Treść: Tak magiczny email, że oczarował nawet mnie!

### 🤔 Co trzeba zrobić?

- Utwórz obiekt wiadomości (`EmailMessage`).
- Ustaw `subject`, `from`, `to`, `set_content(...)`.
- Połącz się z serwerem SMTP (`smtplib.SMTP_SSL`).
- Wyślij maila (`smtp.send_message(msg)`).
- Zamknij połączenie i sprawdź skrzynkę  
  *(lub użyj `with`, wtedy sesja zamknie się automatycznie)*.


### Podpowiedzi - krok po kroku **

Utwórz obiek wiadomości, poszukaj jakie możliwości Ci daje  `EmailMessage()`
```
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



> TIP
> Jeśli zobaczysz błąd smtplib.SMTPAuthenticationError, upewnij się, że:
> używasz klucza aplikacji, a nie zwykłego hasła,
> konto ma włączone 2-etapowe logowanie,
> podajesz poprawny port (465) i wykorzystujesz SMTP_SSL.
{: .block-tip}


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

🤔 **Co trzeba zrobić?**

- Odczytaj `stolik.csv` — użyj dowolnej poznanej metody.  
- Dla każdej osoby:  
  - wczytaj treść `szablon.txt`,  
  - podmień `{imie}` na imię z pliku,  
  - utwórz wiadomość (`EmailMessage`),  
  - ustaw temat, nadawcę, odbiorcę, treść,  
  - wyślij przez SMTP.  

Po wysyłce wypisz w konsoli np. `Wysłano do: Harry <harry@example.com>`.

> ##### TIP
>
> W pętli `for` przypomnisz sobie `enumerate()` lub klasyczne iterowanie list.
{: .block-tip }