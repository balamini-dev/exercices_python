import os

#ex1

def double(n):
    res=n*2
    return res
    print(res)

n=int(input("entrer entier : "))
print("le double de ",n, "est ",double(n)) #appel de la fonction

#ex4

def max3(x1,x2,x3):
    if x1>=x2 and x1>=x3:
        return x1
    elif x2>=x3 and x2>=x3:
        return x2
    else:
        return x3
x1 = int(input("saisir x1 = "))
x2 = int(input("saisir x2 = "))
x3 = int(input("saisir x3 = "))

print("la plus grande des trois valeurs est : ",max3(x1,x2,x3)) #appel de la fonction

#ex6

def inverse(a,b):
    c=0
    c=a
    a=b
    b=c
    return(a,b)

a=int(input("entrer le nb 1 : "))
b=int(input("entrer le nb 2 : "))
inverse=(inverse(a,b)) #appel de la fonction
print("le nb 1 est devenu", b, " et le nb 2 est devenu",a,)

#ex7 à finir

def calculPrix(nbcopies):
    if nbcopies<=10:
        return (nbcopies*10)/100
    elif nbcopies<=30:
        return(10*10+(nbcopies-10)*8)/100
    else:
        return(10*10+20*8+(11-30)*7)/100

nbcopies=int(input("nombre de copies ? "))
prix = calculPrix(nbcopies)
print(prix)


#ex8

def bissextile(annee):
    nbJours=0
    if annee>0:
        if annee%4 !=0:
            nbJours=28
        elif annee%100!=0:
            nbJours=29
        elif annee % 100!=0:
            nbJours=28
        else:
            nbJours=29
        return(nbJours)
    else:
        nbJours=0

annee=int(input('entrer une année : '))
if bissextile(annee)==29:
    print(annee," est une année bissextile car le nb de jour du mois de février est de ",bissextile(annee), "jours.")
elif bissextile(annee)==28:
    print(annee," n'est pas une année bissextile car le nb de jour du mois de février est de ",bissextile(annee), "jours.")
else:
    print(annee," n'est pas une année valable")



#ex9 à finir

def menu(exo):
    continuer = ""
    res=os.system("cls")
    while continuer!="q":
        if(exo)==1:
            return double(n)
        if(exo)==4:
            return max3(x1,x2,x3)
        if(exo)==6:
            return inverse(a,b)
        if(exo)==7:
            return calculPrix(nbcopies)
        if(exo)==8:
            return bissextile(annee)
        continuer = input("stop ou encore ? Taper q pour quitter.")

exo=int(input("entrez un numéro d'exercice : "))
print(menu(exo))



########################ex9 correction###########################


continer ="oui"
while continer !="q":
    res=ossystem("cls")
    print("choix 1 : premier")
    print("choix 2 : somme")
    choix=int(input('entrer un choix ? : '))
    if(choix==1):
        n=int(input('n? : '))
        print(premeier(n))
    if(choix==2):
        n=int(input('n? : '))
        print(somme(n))
    continuer = input('stop ou encore ? Taper q pour quitter')
            
    
