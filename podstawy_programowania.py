co2 = [750, 990, 1100, 880, 1240, 1180, 1050, 820, 1300, 970]
prog = 1000

liczba_przekroczen = 0
suma_przekroczen = 0

for odczyt in co2:
    if odczyt > prog:
        liczba_przekroczen += 1
        suma_przekroczen += odczyt - prog

if liczba_przekroczen >= 3:
    decyzja = "TAK"
else:
    decyzja = "NIE"

print("liczba przekroczen:", liczba_przekroczen)
print("suma przekroczen:", suma_przekroczen)
print("czy trzeba zmienić sposob wietrzenia:", decyzja)
