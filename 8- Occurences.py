continuer = True
while continuer:
    
##################################################################
        



    texte=str(input("entrer votre texte svp :  "))
    a=0

    for i in range (len(texte)):
        if texte[i] == "P":
            if texte[i+1] == "R":
                if texte[i+2] == "O":
                    if texte[i+3] == "G":
                        if texte[i+4] == "R":
                            if texte[i+5] == "A":
                                if texte[i+6] == "M":
                                    if texte[i+7] == "M":
                                        if texte[i+8] == "E":
                

                                                            a=a+1
    print(a)


##################################################################
        
    choix = input("Voulez vous entrer un autre texte ? ")
    if choix not in ('o', 'oui', 'ok'):
        continuer = False
