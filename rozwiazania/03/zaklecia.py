def przywitaj(imie):
    print(f"Witaj, {imie}! Twoja przygoda w Hogwarcie się zaczyna!")

def filter_spells(text, banned):
    new_text = text
    for spell in banned:
        new_text = new_text.replace(spell, "***").replace(spell.capitalize(), "***")
    return new_text