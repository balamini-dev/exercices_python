def F(a, b, c):
    
    global Liste_divA
    global Liste_divB
    global Liste_divC

    Liste_divA = []
    Liste_divB = []
    Liste_divC = []

    diva=1
    divb=1
    divc=1
    
    while diva <= a :
        if a%diva == 0:
            Liste_divA.append(diva)
        diva+=1

    while divb <= b :
        if b%divb == 0:
            Liste_divB.append(divb)
        divb+=1

    while divc <= c :
        if c%divc == 0:
            Liste_divC.append(divc)
        divc+=1


    print(Liste_divA)
    print(Liste_divB)
    print(Liste_divC)

    global abc
    abc=[a,b,c]

def commun():
    comm=[]
    for i in range(len(Liste_divA)):
        if Liste_divA[i] in Liste_divB and Liste_divA[i] in Liste_divC :
            comm.append(Liste_divA[i])

    x = 0

    for i in range(len(comm)):
        if comm[i]>x:
            x=comm[i]
    print("Le PGCD de",abc[0],"de",abc[1],"et de",abc[2], "est : ", x)
