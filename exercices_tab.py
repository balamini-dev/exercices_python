'''
#BASE
#ex1
def tableau(tab):
    a=0
    tab.append(5)
    for i in range(0,len(tab)):
        a=a+tab[i]
    print(a)
    return(tab)
tab=[2,8,3,7]
tableau(tab)
print(tab)


#ex2
tab=[2,98,3,788]
def maxi(tab):
    a=0
    b=0
    for i in range(len(tab)):
        if tab[i]>a:
            a=tab[i]
            b=i
        else:
            a=a
    print("la plus grande valeur du tableau est à l'indice :",b)
    return("la plus grande du tableau est :",a)
print(maxi(tab))


#ex3
tab=[92,98,3,7]
def recherche(tab):
    rep=False
    for i in range(len(tab)):
        if tab[i]==2:
            rep=True
            break
        else:
            rep=False
    return(rep)
print(recherche(tab))

#AVANCÉ
#ex2
tab=[52,899,3,7]
def inversion(tab):
    tabInv=[]
    for i in range(len(tab)):
        tabInv.append(tab[3-i])
    print("le tableau d'origine est : ",tab)
    return("le tableau inversé est : ",tabInv)
print(inversion(tab))

#ex2v2
tab=[52,899,3,7]
n=len(tab)
def inversion(tab):899

    for i in range (round(n/2)):
        tmp=tab[i]
        tab[i]=tab[n-1-i]
        tab[n-1-i]=tmp
    return(tab)
print(inversion(tab))


#ex4 fonction de décalage vers le haut

tab=[2,8,1,7]
def decal_h(tab):
    tmp=tab[0]
    for i in range(1, len(tab)):
        tab[i-1]=tab[i]
    tab[len(tab)-1=tmp]
    

#ex5 fonction de décalage vers le bas

tab=[2,8,1,7]
def decal_b(tab):
    tmp=len(tab)-1
    for i in range(len(tab)-1,0,-1):
        tab[i]=tab[i-1]
    tab[0]=tmp
    
    

#ex7
b=0
def suppElt(tab, val): #ES : tab - E valeur à supprimer
    n=len(tab)
    for i in range(0,n):
        if tab[i]==val:
            for j in range (i+1, n):
                tab[j-1]=tab[j]
            tab.pop()
            return True
    return False #dès lors qu'un return est exécuté, le reste du code ne sera pas éxécuté
    
tab=[52,89,3,7]
print(tab)
res=suppElt(tab, 3)
print("supprime ? ", res)
print(tab)

res=suppElt(tab, 52)
print("supprimé ? ", res)
print(tab)

'''

#ex 9

tab=[2,6,9,9,11]
def tri(tab):
    n=len(tab)
    tmp=0
    tmp2=0
    for i in range(n):
        tmp=tab[i]
        if tab[i+1]==tmp:
            for i in range(len(tab)-1,0,-1):
                tab[i]=tab[i-1]
                tab[0]=tmp2
            
print(tri(tab))
