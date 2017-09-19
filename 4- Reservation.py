F=[False]*30
NF=[False]*30



pl_fumeur = 0
pl_Nfumeur = 0

continuer = True
while continuer:
    
##################################################################

        demande = input("Voulez vous un place fumeur (F), une place non fumeur (NF) ou arreter la réservation (AR) : ")
        if demande == "F":
                if pl_fumeur < 30:
                        pl_fumeur+=1
                        F[pl_fumeur]=True
                else:
                        print ("Il n'y a plus de place fumeur.")

        if demande == "NF":
                if pl_Nfumeur < 30:
                        pl_Nfumeur+=1
                        F[pl_Nfumeur]=True
                else:
                        print ("Il n'y pa plus de place non fumeur.")

        if demande =='AR':
                print ("Merci de votre visite et à bientôt !")

        print("il reste : "+ str(30 - pl_fumeur)+" fumeur")
        print("il reste : "+ str(30 - pl_Nfumeur)+" non fumeur")

##################################################################
        
        choix = input("Voulez vous entrer un autre texte ? ")
        if choix.lower() not in ('o', 'oui', 'ok'): # le nom de la variable suivit de .lower() permet gérer les majuscules.
                continuer = False

