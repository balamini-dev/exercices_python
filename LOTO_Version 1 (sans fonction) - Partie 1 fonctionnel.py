import random

grille_visiteur=[0]*6

for i in range (len(grille_visiteur)):
        numero_visiteur = int(input("veuillez entrer 1 numéro compris entre 1 et 49 : "))
        grille_visiteur[i]= numero_visiteur

print("Votre grille est : ")
print(grille_visiteur)
        


grille_loto=[0]*6

for i in range (len(grille_loto)):
        grille_loto[i] = random.randint(1, 9)
print(grille_loto)

grille_final =[0]*6
for i in range (len(grille_visiteur)):
        if grille_visiteur[i] in grille_loto:
                grille_final[i]=grille_visiteur[i]
print(grille_final)

print("Vous avez trouvé le ou les numéros : ")
for i in range(len(grille_final)):
        if grille_final[i]!=0:
                print(grille_final[i])
