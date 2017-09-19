grille = [['M','A','I','S','O'],['N','B','C','D','E'],['F','G','H','K','L'],['P','Q','R','T','U'],['V','W','X','Y','Z']]

def Affiche_carre(l):

    for i in range (len(l)):
        for j in range (len(l[i])):
            print(l[i][j]," ", end='')
            if j == 4:
                print("o")
                
Affiche_carre(grille)


#def Codage_Grille(mot):

mot = input ("Veuillezaisir votre mot : ")

grille = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nT=[[],[],[],[],[]]
x=0
for i in range(len(grille)):
    if grille[i] in mot:
        nT[i]=T[i]
