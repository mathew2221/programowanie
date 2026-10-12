import random

sekret = random.randint(1,10)
proba = 1
maks_prob = 3
zgadlem = False

while proba <= maks_prob and zgadlem == False:
    liczba=int(input("Podaj liczbe od 1 do 10: "))

    if liczba == sekret:
        print("Brawo zgadłeś")
        zgadlem = True
    elif liczba < sekret:
        print("Za mała")
    else:
        print("Za duża")

    proba+=1
if zgadlem == False:
    print(f"nie udało się zgadnać, sekretna liczba to {sekret}")
