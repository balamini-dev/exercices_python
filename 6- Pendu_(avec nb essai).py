continuer = True
while continuer:
    
##################################################################

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

        partie = False
        nb_essai = 10
        while("*") in T:
               
                if nb_essai==0:
                        break
                print("Il vous reste",nb_essai,"essai.")
                lettre = input("entrer votre lettre : ")
                if lettre in mot:
                       for i in range(len(mot)):
                               if mot[i]==lettre:
                                       T[i]=lettre
                                       print(T)
                else:
                        nb_essai -= 1
        if ("*") in T:
                partie = False
        else:
                partie = True

        if partie == True:
                print("Gagné ! =), vous avez touvé le mot <<<",mot,">>>")
        else:
                print("Perdu ! =( ")


##################################################################
        
        choix = input("Voulez vous continuer [o / n] ? ")
        if choix not in ('o', 'oui', 'ok'):
                continuer = False

