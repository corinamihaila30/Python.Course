#declarare lista
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)
#afisare numere ascendent
lista.sort()
print(lista)
#afisare numere descendent
lista.sort(reverse=True)
print(lista)
#numere pare
sublista = slice(1, 7)
lista_scurta = lista[sublista]
print(lista_scurta)
nr_pare=[]
for i in lista_scurta:
    if i % 2 == 0:
        nr_pare.append(i)
print(nr_pare)
#numere impare
nr_impare = []
for z in lista_scurta:
    if z%2 != 0:
        nr_impare.append(z)
print(nr_impare)