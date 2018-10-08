# exercice4
for i in range(1,4):
    for j in range(1,4-i):
        print(' ', end='')
    for k in range(1,i*2):
        print('*')
# exercice5
for i in range(1,4):
    for j in range(1,4-1):
        print(' ', end='')
    for j in range (1, i-1):
        print('*')
    print('|')
    for j in range(1,i-1):
        print('*', end='')
    print('')
for i in range(1,4-1):
    print(' ', end='')
print('|', end='')
print('')


n=int(input('donner n'))
for x in range(0,n):
	print (x*"*")
# inverse 
n=int(input('donner n'))
for x in range(n,0,-1):
	print (x*"*")
