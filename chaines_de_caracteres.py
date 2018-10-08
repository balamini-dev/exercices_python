'''#palindrome
def palindrome(mot): #E: mot S:booleen (vrai si palindrome)
    palindrome=True
    lgmot=len(mot)
    while palindrome==True:
        for i in range(lgmot):
            if mot[i]==mot[(lgmot-1)-i]:
                palindrome=True
            else:
                palindrome=False
                break
    if palindrome==True:
        print("ce mot est un palindrome.")
    else:
        print("ce mot n'est pas un palindrome.")
    return(palindrome)
    
mot=input("veuillez entrer un mot : ")
print(palindrome(mot))

#palindrome 2
def palindrome(mot): #E: mot S:booleen (vrai si palindrome)
    lgmot=len(mot)
    for i in range(lgmot):
        if mot[i]!= mot[(lgmot-1)-i]:
            return False
    return True

    return(palindrome(mot))
    
mot=input("veuillez entrer un mot : ")
print(palindrome(mot))
'''

#anagramme
def anagramme(texte1, texte2):
    n1=len(texte1) #####
    n2=len(texte2) #####
     
    if texte1!=texte2:
        return False
    
    for i in range(0, len(texte1)-1):
        if texte1[i]==" ":
            continue
        trouve=False
        for j in range(0, len(texte2)-1):
            if texte2[j]==" ":
                continue
            if texte1[i]==texte2[j]:
                texte2[j]=" "
                trouve = True
                break
        if trouve==False:
            return False
        
texte1= "Dans ma maison"
texte2= "Dans ma maison"
print(anagramme(texte1, texte2))
