print("--- System postaci ---")
print("Tworzenie nowego bohatera")

imie = input("Podaj imię: ")
poziom = 1
zdrowie = 100
obrazenia = 10
zyje = True


#lewelowanie bohatera

zdrowie = 100 + poziom*10
obrazenia = 10 + poziom*5

#dane przeciwnika

typPrzeciwnika ="tusk"
zyciePrzeciwnika = 60
atakPrzeciwnika = 20

#wybór klasy postaci

print("1 ryczerz 2 assasin 3 mag")
if wybor==1:
    zdrowie=300
    atak=80
    elif wybor==2:
        zdrowie=100
        atak=150
        elif wybor==3:
            zdrowie=150
            atak=100
            else:
                print("niepoprawny wybór")

#print("Imie",imie)
#print("Poziom",poziom)
#print("Punkty życia",zdrowie)

print(f"Imie: {imie}")
print(f"Poziom: {poziom}")
print(f"Punkty życia: {zdrowie}")

print(type(zdrowie))
print(f"{imie} spotkał {typPrzeciwnika} traci {atakPrzeciwnika} pkt życia")
zdrowie = zdrowie - atakPrzeciwnika

print(f"Aktualne punkty życia: {zdrowie}")


