import os
continuer = 'true'
while continuer == 'true':
    if continuer == 'true':
        print("somme des nombres")
        n = int(input('n ? : '))
        som=0
        for i in range(1,n+1):
            som=som+i
            print(som)

        print("somme des nombres paires")
        n = int(input('n ? : '))
        som=0
        for i in range(2,n+1,2):
            som=som+i
            print(som)
            rep=input("continuer ? ");
            if rep == 'o':
                continuer='true'
            elif rep == 'n':
                continer='false'
                res=os.system("cls")

'''
stop=""
while stop!="q":
    res=os.system("cls")
    n = int(input('entrez un entier : '))
    som=0
    for i in range(1, n+1):
        som=som+1
    print("La somme des ",n,"premiers nombres = ",som)
    print()
    stop = input("Stop ou encore ? taper q pour continuer : ")

'''
