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


5.
