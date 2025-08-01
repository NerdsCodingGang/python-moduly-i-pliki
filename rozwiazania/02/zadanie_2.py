import datetime

today = datetime.datetime.now()

# różne formaty
print(today.strftime("%Y-%m-%d"))           # YYYY-MM-DD
print(today.strftime("%d.%m.%Y"))           # DD.MM.YYYY
print(today.strftime("%A, %d %B %Y"))       # Dzień tygodnia, DD Miesiąc YYYY
print(today.isoformat())                    # Format ISO
