def nbConsecutif(tab):
    a=True
    for i in range(1,len(tab)):
        if (tab[i])-(tab[i]-1)!=1:
            a=False
            break
    if a==True:
        print("le tableau est consécutif")
    else:
        print("le tableau n'est pas consécutif")
            
    return(tab)
tab=[]
n1=int(input("nb 1 : "))
tab.append(n1)
n2=int(input("nb 2 : "))
tab.append(n2)
n3=int(input("nb 3 : "))
tab.append(n3)
print(nbConsecutif(tab))
 
######### à finir        http://pise.info/algo/enonces7.htm
