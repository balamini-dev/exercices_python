print("somme des nombres")
n = int(input('n ? : '))
som=0
for i in range(1,n+1):
    som=som+i
print(som)

print("somme des nombres paires")
n = int(input('n ? : '))
som=0
for i in range(2,n+1,2):
    som=som+i
print(som)
