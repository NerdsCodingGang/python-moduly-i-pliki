from openpyxl import Workbook

wb = Workbook()
arkusz = wb.active

arkusz.append(["Zaklęcie", "Efekt"])
arkusz.append(["Lumos", "Światło"])
arkusz.append(["Accio", "Przywołanie przedmiotu"])

wb.save("zaklecia.xlsx")
print("✓ Zapisane")
