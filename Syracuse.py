continuer = True
while continuer:
    

    n = int(input("VEUILLEZ SAISIR UN NUMERO : "))
    tv = n 
    T=[]
    i = 0
    tvol = 0

    T.append(n)
    

    while i < 20:
        print(n)

        if n%2 == 0:
            n = n//2
        else:
            n=(n*3)+1
        i+=1

        T.append(n)
    print(T)

######################### temps de vol
    for i in range(len(T)):
        if T[i] != 1:
            tvol+=1
        else:
            break
    print("le temps de vol de",tv,"est : ")
    print(tvol)
#########################
    
    choix = input("Voulez vous continuer ? ")
    if choix not in ('o', 'oui', 'ok'):
        continuer = False
