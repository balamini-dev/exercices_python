def estIlPremier(p):
# fonction permettant de savoir si un nombre est premier ou non.
        global i # le mot clef < global > permet d'avoir accès à une variable à travers tout le code. Sans ce mot clef la variable est uniquement accessible dans la fontion.
        i = 2
        global booleen
        booleen = True
        while i < p:
                if p%i == 0:
                        booleen = False
                global k
                i = i+1
        return booleen

print(estIlPremier(7))

def listPremier(n):
# fonction permettant d'afficher dans un tableau tous les nombres premiers jusqu'à un nombre (n).
        global j
        j = 0
        global l
        l = []
        for j in range(2,n+1): # on parcours les nombres allant de 2 à (n+1). Si on ne spécifie pas (n+1) il va s'arréter à l'élément qu'il y a juste avant le (n) sans le lire. 
                if estIlPremier(j):
                        l.append(j)
        return l

print(listPremier(7))


def programme3():
        
        n = int(input("Saisir un entier pair supérieur à 1 : "))
        print (estIlPremier(n)) # réutilisation de la fonction (estIlPremier)
        if booleen == True :
                print(n, "est un nombre premier")
        else:
                print(n, "n'est pas un nombre premier")

        print("\n")
        print("Voici la liste des nombres premiers allant jusqu'à : ",n)
        print(listPremier(n)) # réutilisation de la fonction (listPremier)
        print("\n")

        moitieN = n/2 # la moitié de (n)
        moitieNarr = n//2 # la moitié de (n) à l'arrondi
        
        if moitieN in l:
                print("on peut décomposer ",n," en une somme de deux nombres premiers comme ce qui suit : ")
                print(n," = ",moitieNarr,"+",moitieNarr)

##################
# B.4 à comparer #
##################

        T=[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
        for i in range(len(T)):
                moitieN2 = T[i] / 2
                moitieN2arr = T[i] // 2

                if moitieN2 in l:
                        print(moitieN2arr)
        print("\n")
        print("Pour une liste de nombre pairs compris entre 4 et 50 ces entiers sont la décomposition en une somme de deux nombre des nombres premiers, exemeple 4 = 2*2 et 2 sera affiché car c'est un nombre premier.")
                        
