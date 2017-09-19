continuer = True
while continuer:
    
##################################################################
    
    mot= str(input("votre mot est : "))
    palindrome = False
    f = len(mot)
    m = len(mot)//2

    for i in range(m):
        f=f-1
    if mot[i]==mot[f]:
        print("ceci est un palindrome")
    else:
        print("Ceci n'est pas un palindrome")
        
##################################################################
        
    choix = input("Voulez vous continuer ? ")
    if choix not in ('o', 'oui', 'ok'):
        continuer = False
