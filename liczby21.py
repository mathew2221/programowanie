imie=input("Podaj imię: ")
liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

suma=liczba1 + liczba2

if suma > 10:
    print(f"Witaj {imie} suma: {suma} jest większa od 10")
else:
    print(f"Witaj {imie} suma: {suma} jest mniejsza od 10")
