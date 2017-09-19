def nb_commun():
    nbc=0
    T1=[8,2,6]
    T2=[1,91,7]

    for i in range(len(T1)):
                
            if T1[i]==T2[i]:
                nbc=nbc+1
              
            else:
                pass
    print("il y a ", nbc, " nombre(s) en commun dans les deux tableaux")
    
 
