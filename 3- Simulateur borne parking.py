n=1
continuer = True
while continuer == True:

######################################################################################################################################################################

    pieces_accepte = [10, 5, 2, 1, 0.5]

    tarif_heure = 2


    hA = float(input("ticket n°" + str(n) + " veuillez entrer l'heure d'arrivé (en séparant les heures des minutes avec une point) : ")) # on transforme le int en string pour qu'il soit afficher, mais en aucun cas il son type est changé dans le programme.
    while hA <0 or hA >= 24:
        hA = int(input("ticket n°" + str(n) + " HEURE NON VALIDE! Veuillez entrer l'heure d'arrivé : "))
        

    hD = float(input("Vous avez introduit le ticket n°" + str(n) + " veuillez entrer l'heure de départ (en séparant les heures des minutes avec une point) : "))
    while hD <0 or hD >= 24:
        hD = int(input("ticket n°" + str(n) + " HEURE NON VALIDE! Veuillez entrer l'heure de départ : "))

    temps_stationnement = hD - hA

    prix_stationnement = temps_stationnement*2
    prix_stationnement = round(prix_stationnement,2)


    print("Prix : " ,str(prix_stationnement)+ "€")


    while prix_stationnement > 0:
        paiement = int(input("Il reste à payer :" + str(prix_stationnement) + " €. Seulement les pièces de 10f, 5f, 2f, 1f, 0.5f sont acceptés : "))
        if paiement in pieces_accepte:
            prix_stationnement -= paiement
        else:
            print("PIECE NON VALIDE, INSERER UNE PIECE DE [ 10f, 5f, 2f, 1f, 0.5f ] SVP.")

    if prix_stationnement < 0:
        prix_stationnement = abs(prix_stationnement) # convertir nombre négatif en positif
        prix_stationnement = round(prix_stationnement,2)

        print("Votre monnaie est de " +str(prix_stationnement)+ "€. N'oubliez pas votre monnaie et à bientôt.")

    n+=1

#####################################################################################################################################################################
    O_N = input("Voulez vous prendre un ticket ? oui(o) / non (n) ? ")
    if O_N == "n":
        continuer = False
    elif O_N == "o" :
        continuer = True
    else :
        continuer = False







#Axes d'améliorarion : Faire un tableau qui regroupe les heures et parcourir ce tableau et voir l'écart entre l'heure de départ et l'heure d'arrivé.
#           Pour gérer le faite que on peut garer la voiture sur deux jours différents ou durant plusieurs jours.
