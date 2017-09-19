continuer  = True
while continuer == True:
        
##################################################################

        texte = input("votre texte : ")
        mot = 0
        phrase = 0

        for i in range (len(texte)):
                if texte[i] == " " or texte[i] == "." and texte[i-1]!=" ":
                                mot+=1
                                
                if texte[i] == "." and texte[i-1]!= ".":
                                phrase+=1

                if phrase > 1:
                        mot = mot - 1

        print(texte)
        print("votre texte contient ",mot, " mot(s) et ",phrase," phrase(s).")
##################################################################

        choix = input("Voulez vous entrer un autre texte ? \n oui ou non : ")
        if choix not in ('o', 'oui', 'ok'):
                continuer = False
