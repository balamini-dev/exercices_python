MAT = [[30,67,100],[43,59,69],[73,83,92]]

def ecrire_math(MAT):
    for i in range(len(MAT)):
        for j in range(0,3):
            print(MAT[i][j],end=' ')
        print()
    print()
ecrire_math(MAT)

###############################################

def luminosité(MAT):
    global m
    m = 0
    for i in range(len(MAT)):
        for j in range(0,3):
            m = m + MAT[i][j]
    m=m//9
    
    print(m)
    print()
luminosité(MAT)

###############################################

def contraste(MAT, luminosité):
    for i in range(len(MAT)):
        for j in range(0,3):
            if MAT[i][j] <= m:
                MAT[i][j] = MAT[i][j]//2
            else:
                MAT[i][j] = MAT[i][j]*2
                if MAT[i][j] > 100:
                    MAT[i][j] = 100
    ecrire_math(MAT)
    print()

contraste(MAT, luminosité)





#https://bts-sio-formation.com/U22

