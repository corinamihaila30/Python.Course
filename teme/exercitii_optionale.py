1.
list_1 = [-8, 1, 2, -2, 0]

list_2 = [1, 1, 0, 0, 2, -2, -2]

list_3 = [1, -1, 0, -9, 4, -5]

list_4 = [1, 4, 0, 23, 6, 34]

set_1 = sorted(set(list_1))
al_doilea_nr_1 = set_1[1]
print(al_doilea_nr_1)

set_2 = sorted(set(list_2))
al_doilea_nr_2 = set_2[1]
print(al_doilea_nr_2)

set_3 = sorted(set(list_3))
al_doilea_nr_3 = set_3[1]
print(al_doilea_nr_3)

set_4 = sorted(set(list_4))
al_doilea_nr_4 = set_4[1]
print(al_doilea_nr_4)

2.
list_var = ['p', 's']
lista_goala = []
numar = int(input("Scrie un numar:"))
for i in list_var:
    for j in range(1, numar):
        nou = i + str(j)
        lista_goala.append(nou)
print(lista_goala)

3.
n = int(input("Scrie un numar de la 1 la 14: "))
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
rezultat =lista_start[0:n]
print(rezultat)

4.
models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sortarea = sorted(models, key=lambda x: x['make'])

for model in sortarea:
    print(model)
