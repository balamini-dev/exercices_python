import random

MT=["bateau", "giraphe", "clochard", "serpent", "poubelle", "cheval", "medecin", "cité", "antibiotique", "stylo", "football"]

# Obtenir un élément au hasard  
i = random.randint(0, len(MT)-1)  
mot = MT[i] 

nb_lettres = 0

for i in range(len(mot)):
        nb_lettres +=1
print("mot contenant",nb_lettres,"lettres")        
T = ['*']*nb_lettres
T[0]=mot[0]
print(T)

while("*") in T:
        lettre = input("entrer votre lettre : ")
        if lettre in mot:
               for i in range(len(mot)):
                       if mot[i]==lettre:
                               T[i]=lettre
                               print(T)

print("partie terminé, vous avez touvé le mot <<<",mot,">>>")


# faire une autre version du jeu avec un compteur d'essai
