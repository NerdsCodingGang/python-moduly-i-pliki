import zaklecia

banned_spells = ["avada", "imperi", "crucio"]

texts = [
    "Zaklęcie niewybaczalne to Avada Kedavra",
    "W pojedynku Crucio użyte na przeciwniku jest zakazane.",
    "Alohomora otwiera wiele drzwi."
]

for t in texts:
    print(zaklecia.filter_spells(t, banned_spells))
