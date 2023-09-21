#1.
#lista = [1, 2, 3, 4, 5, 6, 7]
#k=3
def functie(lista, k):
    lungime = len(lista)
    if (k > lungime - 1):
        print("Eroare. Valoarea lui k este prea mare.")
    while (k != 0):
        lista.insert(0, lista[lungime - 1])
        lista.pop()
        k -= 1
    return lista

listaNoua = functie(lista,k)
print(listaNoua)

#2.
#apMax = aparatie maxima
#lista = [2, 2, 1, 1, 1, 2, 2]
def gasesteMax(lista):
    apMax = 0
    s = ""
    for i in lista:
        if lista.count(i) > apMax:
            apMax = lista.count(i)
    valoriDistincte = set(lista)
    for i in valoriDistincte:
        if lista.count(i) == apMax:
            s = s + str(i) + ", "
    s = s[0:len(s)-2]
    return s

s = gasesteMax(lista)
print(s)
