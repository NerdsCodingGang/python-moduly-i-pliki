import requests  # korzystamy z pakietu requests

# pobranie danych z API
req = requests.get("http://numbersapi.com/random/year")
text_from_api = req.text
print("Tekst z API:", text_from_api)


if "13" in text_from_api: # sprawdzenie czy jest liczba 13
    print("✅ Tekst zawiera liczbę 13")
else:
    print("❌ Tekst nie zawiera liczby 13")

user_input = input("Podaj dowolny ciąg znaków: ") # pytanie użytkownika o dowolny ciąg znaków
user_input = user_input.lower()

if user_input in text_from_api.lower(): # sprawdzenie czy tekst zawiera ciąg użytkownika
    print("✅ Tekst zawiera Twój ciąg znaków")
else:
    print("❌ Tekst nie zawiera Twojego ciągu znaków")
