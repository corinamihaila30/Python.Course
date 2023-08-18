1.
text= input("Textul de verificat este:")
variabila= "Mihai"
gasit = False
for i in text:
    if not i.isdigit() and not i==" " and gasit == False:
        gasit = True
        print("Sirul de caractere a fost gasit de", variabila)
if gasit == False:
    print("Sirul de numere a fost gasit de", variabila)


2.
numar= int(input("Numarul de verificat este:"))
if numar%2==0:
    print("Numarul este par")
else:
    print("Numarul este impar")


3.
numar= int(input("Anul de verificat este:"))
if numar%4==0:
    print("Anul este bisect")
else:
    print("Anul nu este bisect")


4.
numar=int(input("Numarul de verificat este:"))
if numar>0 and numar<10:
    print("Numarul este pozitiv")
elif numar<0:
    rezultat= abs(numar)
    print(rezultat)
elif numar==0:
    print("Numarul este 0.")
else:
    print("Numarul de verificat nu e valid")


5.# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

lista = []
while True:
    print("""
    1 – Afisare lista de cumparaturi
    2 – Adaugare element
    3 – Stergere element
    4 – Stergere lista de cumparaturi
    5 - Cautare in lista de cumparaturi
    6 - Iesire
    """)

    numar = int(input("Introduceți numărul opțiunii: "))

    if numar == 1:
        print("Lista de cumpărături:", lista)
    elif numar == 2:
        produs = input("Introduceți numele produsului: ")
        lista.append(produs)
        print(f"Elementul '{produs}' a fost adăugat în listă.")
    elif numar == 3:
        produs = input("Introduceți elementul de șters: ")
        if produs in lista:
            lista.remove(produs)
            print(f"Elementul '{produs}' a fost șters din listă.")
        else:
            print(f"Elementul '{produs}' nu a fost găsit în listă.")
    elif numar == 4:
        lista.clear()
        print("Lista de cumpărături a fost ștearsă.")
    elif numar == 5:
        produs = input("Introduceți elementul de căutat: ")
        if produs in lista:
            print(f"Elementul '{produs}' a fost găsit în listă.")
        else:
            print(f"Elementul '{produs}' nu a fost găsit în listă.")
    elif numar == 6:
        print("Meniul a fost închis.")
        break
    else:
        print("Alegerea nu există. Reîncercați.")
