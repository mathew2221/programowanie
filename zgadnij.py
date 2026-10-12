dol = 1
gora = 100

print("Pomyśl liczbe od 1 do 100")
print("Będę próbował ją odgadnąć")

while dol <= gora:
    srodek = (dol + gora) // 2

    print("Czy Twoja liczba to", srodek)
    odpowiedz = input("Wpisz: m - mniejsza, w - większa, t - trafiona: ")

    if odpowiedz == "t":
        print("Zgadłem!")
        dol = gora + 1

    elif odpowiedz == "m":
        gora = srodek + 1

    elif odpowiedz == "w":
        dol = srodek + 1
