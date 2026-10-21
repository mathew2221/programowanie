pensje = [4200, 5100, 4800, 4500, 4700, 5300, 4900, 35000, 4400]

for i in range(len(pensje) - 1):
    for j in range(len(pensje) - 1):
        if pensje[j] > pensje[j + 1]:
            temp=pensje[j]
            pensje[j]=pensje[j+1]
            pensje[j+1]=temp
    print(f"{i+1}:", pensje)

sr = sum(pensje) / len(pensje)
print("Min:", pensje[0], "Max:", pensje[-1], "Średnia:", round(sr, 2), "Mediana:", pensje[len(pensje)//2], "Rozstęp:", pensje[-1] - pensje[0])
print("Mniej niż średnia:", sum(1 for p in pensje if p < sr))
print("Srednia bez prezesa:", sum(pensje[:-1]) / (len(pensje) - 1))
print("Hasło prawdziwe matematycznie, ale mylące (8 osób zarabia poniżej średniej).")

pensje.append(6000)
for i in range(len(pensje) - 1):
    for j in range(len(pensje) - 1):
        if pensje[j] > pensje[j + 1]:
            temp = pensje[j]
            pensje[j] = pensje[j + 1]
            pensje[j + 1] = temp

print("Nowa lista:", pensje)
print("Nowa mediana:", (pensje[4] + pensje[5]) / 2)
