def trouverNb():
    import random
    continuer=True
    while continuer==True:
        nbBase = random.randint(1,1000)
        print(nbBase)
        n=int(input("Le nombre que vous devez trouver est entre 1 et 1000. "))
        gagne=False

        while gagne==False:
            if n!=nbBase:
                if n>nbBase:
                    print("trop grand")
                    n=int(input("entrer un nombre est entre 1 et 1000. "))
                else:
                    print("trop petit")
                    n=int(input("entrer un nombre est entre 1 et 1000. "))
            else:
                print("nombre trouvé =D")
                gagne=True
                break
        reponse=input("voulez vous continuer ? : (o/n) ")
        if reponse!=("o"):
            continuer=False
        else:
            continuer=True
    return(nbBase)

print(trouverNb())
