# Nicolas Siarri SLAM 02/03/2017
def init():

    tab_porte = []
    
    for num_porte in range(1000):
        tab_porte.append([num_porte, False])


    return tab_porte



def etape() :
    
    porte_finale = []
    
    for operation in range (1,1001) :
        for porte in tab_porte :
            if porte[0] % operation == 0 :
                if porte[1] == False :
                   
                       porte[1] = True
                                    
                elif porte[1] == True :
                    porte[1] = False
            else :
                continue
    
    return tab_porte

def final(tab_porte):
    cpt = 0
    for etat in tab_porte :
        if etat[1] == True :
            cpt += 1
            if cpt == 23:
                print(etat[0])
                break
            else :
                continue
        

tab_porte =  init()

porte_finale = etape()
result = final(tab_porte)
