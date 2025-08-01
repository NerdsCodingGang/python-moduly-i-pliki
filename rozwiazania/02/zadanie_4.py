import requests


API_KEY = "YOUR_API_KEY"  # wstaw swój klucz API
API_URL = "http://api.openweathermap.org/data/2.5/weather"

# ---- funkcje ----
def choose_country():
    print("Wybierz kraj:")
    print("1. United Kingdom - uk")
    print("2. Poland - pl")
    print("3. Germany - de")
    
    choice = input("Podaj numer kraju: ")
    
    if choice == "1":
        return "uk"
    elif choice == "2":
        return "pl"
    elif choice == "3":
        return "de"
    else:
        print("Niepoprawny wybór, ustawiam domyślnie Poland (pl).")
        return "pl"

def get_city():
    return input("Podaj nazwę miasta: ")

def get_weather(city, country):
    api_url = f"{API_URL}?q={city},{country}&appid={API_KEY}&units=metric&lang=pl"
    response = requests.get(api_url)
    return response

def show_weather(response, city):
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Pogoda w {city}: {description}, temperatura: {temp}°C")
    else:
        print("Błąd: nie udało się pobrać danych. Sprawdź miasto, kraj lub klucz API.")

# ---- główny program ----
def main():
    country = choose_country()
    city = get_city()
    response = get_weather(city, country)
    show_weather(response, city)

if __name__ == "__main__":
    main()