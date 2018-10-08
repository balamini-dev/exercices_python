#BOUCLE WHILE
i=1
while i<=10:
    res=7*i
    print(i,' * ',7,' = ',res)
    i=i+1

#BOUCLE FOR
print('\n')
for i in range (1, 11):
    res=7*i
    print(i,' * ',7,' = ',res)

#BOUCLE (CONDITION JAMAIS VERIFIÉ, SORTIR PAR 'break')
print('\n')
i=0
while i>=0:
    res=7*i
    print(i,' * ',7,' = ',res)
    i=i+1
    if i>1000:
        break
    
