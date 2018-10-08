premier = True
n=int(input("veuillez entrer un nb pour savoir s'il est premier : "))
for i in range(2,n):
	if n%i == 0:
		premier = False
		break
if premier ==True:
	print(n," est un nombre premier")
else:
	print(n," n'est pas un nombre premier")

###################################
	
premier = True
n=int(input("veuillez entrer un nb pour savoir s'il est premier : "))
if n%2 == 0:
    premier = False
else:
    i=0
    while i*i <n:
        print(i)
        if n%i==0:
            premier=False
            break
            i=i+2
print(premier)
