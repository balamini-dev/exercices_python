def etape():
    portes = 1000*[False]

    for i in range(len(portes)):
        for j in range(1,1001):
            if (i)%(j)==0:
                if portes[i] == False :
                    portes[i]=True
                else :
                    portes[i]=False
            

    portes_ouvertes = 0
    numero_portes = 0

    print(portes)

    for j in range(len(portes)):
        if portes[j]==True:
            portes_ouvertes+=1
            if portes_ouvertes==23:
                print(numero_portes, "est notre porte! ")
                break
        numero_portes+=1
        
        
etape()
