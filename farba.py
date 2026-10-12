import math

dlugosc=float(input("Podaj długość pokoju: "))
szerokosc=float(input("Podaj szerokość pokoju: "))
wysokosc=float(input("Podaj wysokosc pokoju: "))

powierzchnia= 2 * (dlugosc+szerokosc) * wysokosc

cena=25
wydajnosc=13

ilosc_farby = powierzchnia / wydajnosc

potrzebne_litry = math.ceil(ilosc_farby)

koszt = potrzebne_litry * cena

print(f"Powierzchnia ścian: {powierzchnia}, Potrzebna ilość farby: {potrzebne_litry}, Koszt farby: {koszt}")




              
