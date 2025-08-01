import random
import math

# --- część 1: losowanie liczby i wyświetlenie serduszek ---
number = random.randint(1, 100)  # losuje liczbę od 1 do 100
print("Wylosowana liczba:", number)
print("❤︎" * number)

# --- część 2: logarytmy z liczby 256 ---
value = 256
print("\nLogarytm naturalny:", math.log(value))       # ln(256)
print("Logarytm kwadratowy:", math.log(value, 2))     # log2(256)
print("Logarytm dziesiętny:", math.log10(value))      # log10(256)
