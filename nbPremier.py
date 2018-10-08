def nbPremier(n):
        for i in range(2,n-1):
                if n%i == 0:
                        premier = False
                        break
                else:
                        premier = True
        if premier == True:
                print(n," est un nombre premier")
        else:
                print(n," est n'est pas un nombre premier")
        return(premier)

continuer=True
while continuer==True:
        n=int(input("veuillez entrer un nb pour savoir s'il est premier : "))
        print(nbPremier(n))
        rep=input("continuer ? (o/n): ")
        if rep == "o":
                continuer:True
        else:
                continuer:False
                print("Au revoir ... ")
                break
