tablica1=[2,5,3,7]
tablica2=[5,7,2,9]
tablica3=[tablica1[0]+tablica2[0],tablica1[1]+tablica2[1],tablica1[2]+tablica2[2],tablica1[3]+tablica2[3]]

print(tablica1)
print(tablica2)
print(tablica3)



i_kuba=[int(input("Podaj ilość ocen kuba: "))]
i_jacek=[int(input("Podaj ilość ocen jacek: "))]
i_rafal=[int(input("Podaj ilość ocen rafal: "))]
i_oskar=[int(input("Podaj ilość ocen oskar: "))]

o_kuba=[int(input("Podaj swoje oceny kuba: "))]
o_jacek=[int(input("Podaj swoje oceny jacek: "))]
o_rafal=[int(input("Podaj swoje oceny rafal: "))]
o_oskar=[int(input("Podaj swoje oceny oskar: "))]

sred_kuba=sum(o_kuba)/i_kuba
sred_jacek=sum(o_jacek)/i_jacek
sred_rafal=sum(o_rafal)/i_rafal
sred_oskar=sum(o_oskar)/i_oskar
