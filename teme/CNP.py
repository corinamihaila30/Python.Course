cnp = input("Introdu un CNP: ")
if len(cnp) != 13:
    print("CNP-ul nu are 13 cifre")
else:
    s = int(cnp[0])
    a = int(cnp[1:3])
    l = int(cnp[3:5])
    z = int(cnp[5:7])
    j = int(cnp[7:9])
    n = int(cnp[9:12])
    c = int(cnp[-1])
    if s >= 1 and s <= 9:
        if a >= 0 and a <= 99:
            if (cnp[3] == '0' and 1 <= int(cnp[4]) <= 9) or (10 <= l <= 12):
                if (cnp[5] == '0' and 1 <= int(cnp[6]) <=9 ) or (10 <= z <= 31):
                    if (cnp[7] == '0' and 1 <= int(cnp[8]) <=9 ) or (10 <= j <= 52):
                        if n != 000 and n <= 999:
                            print("CNP valid")
                        else:
                            print("CNP invalid: Valori neregulamentare pentru NN")
                    else:
                        print("CNP invalid: Valori neregulamentare pentru JJ")
                else:
                    print("CNP invalid: Valori neregulamentare pentru ZZ")
            else:
                print("CNP invalid: Valori neregulamentare pentru LL")
        else:
            print("CNP invalid: Valori neregulamentare pentru AA")
    else:
        print("CNP invalid: Valori neregulamentare pentru S")
