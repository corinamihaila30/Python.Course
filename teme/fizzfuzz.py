numar= int(input("Scrie un numar:")) 
if numar%3==0 and numar%5==0:
    print("FizzFuzz")
elif numar%3==0:
    print("Fizz")
elif numar%5==0:
    print("Fuzz")