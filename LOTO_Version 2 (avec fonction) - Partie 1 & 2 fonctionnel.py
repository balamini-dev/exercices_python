import random

grille_visiteur=[0]*6

for i in range(6):
    nombre = int(input("veuillez entrer un nombre compris entre 1 et 49 : "))        
    while nombre in grille_visiteur or nombre < 1 or nombre > 49:
        nombre = int(input("veuillez entrer un autre nombre : "))
    else:
        grille_visiteur[i]=nombre

print("Votre grille est : ")
print(grille_visiteur)

###############################################

    
def numero_tires():

    
    tab = [0]*49
    nb_Tirage = 0
    while nb_Tirage<6:
        resultat=random.randint(1,49)
        if tab[resultat-1]==0:
            tab[resultat-1]=1
            nb_Tirage+=1

    return tab

def resultats():
    tirages=numero_tires()

    global T # pour que la variable (T) soit accessible en dehors de la fonction il faut mettre le mot (global) avant la variable, puis sur une autre ligne affecter une valeur à cette variable.
    T =[0]*6
    num=0

    for i in range(49):
        if tirages[i]==1:
            T[num]=i+1
            num=num+1

    return T
print(resultats())


################################################

grille_final = [0]*6
for i in range(6):
    if grille_visiteur[i] in T:
        grille_final[i]=grille_visiteur[i]
print(grille_final)

print(" Numéros trouvés : ")
for i in range(len(grille_final)):
    if grille_final[i]!=0:
        print(grille_final[i])





        
