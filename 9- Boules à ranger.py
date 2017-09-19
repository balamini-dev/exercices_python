import random 

nb = int(input("Combien de boules souhaitez vous trier ? ")) # nombre de boules, (taille du tableau)

TB=['' for e in range(nb)] # tableau qui contiendra les boules Bleu 
TR=['' for e in range(nb)] # tableau qui contiendra les boules Rouge

T=[random.randint(0,1) for i in range(nb)] # On génere un tableau de chiffre qui sortira aléatoirement 1 ou 0
Tlettres=[] # on crée un tableau qui contiendra R (qui correspond à rouge) pour la valeur 1 et B (qui correspond à bleu) pour la valeur 0 
for item in T : # pour chaque valeur du tableau T
    if item == 1 : # si la valeur vaut 1
        Tlettres.append('R') # alors on met R dans le tableau (Tlettres)
    else :
        Tlettres.append('B') # sinon (ça vaut 0 et donc) on met B dans le tableau (Tlettres)

print(Tlettres) # on affiche le tableau de lettre non rangé.

tri = input("Voulez trier les boules ? \n Entrer O pour (oui) ou  alors entrer N pour (non): ... " )
if tri == "o":
    for i in range(nb): # boucle for qui sera effectué (nb) fois
        if T[i]==0: # on parcours le tableau T, si T[i] == 0 alors :
            TB[i]=T[i] # on met la valeur de T[i] à la place de la valeur de TB[i]
        else:
            TR[i]=T[i] #(sinon c'est forcément égal à 1) donc on met la valeur de T[i] à la place de la valeur de TR[i]

    TB = [i for i in TB if i != ''] # dans le tableau TB on efface les valeurs('')
    TR = [i for i in TR if i != ''] # dans le tableau TR on efface les valeurs('')

else:
    print("au revoir.")

TBR = TB + TR # on concatène les 2 tableaux pour en former un seul


FINAL_TRI = [] # on déclare un dernier tableau dans lequel on mettera à la place de 0, B et à la place de 1, R 

for item in TBR : # pour chaque valeur du tableau TBR
    if item == 1 : # si la valeur vaut 1
        FINAL_TRI.append('R') # alors on met R dans le tableau (FINAL_TRI)
    else :
        FINAL_TRI.append('B') # sinon on met B dans le tableau (FINAL_TRI)

print(FINAL_TRI)
            
