a =int(input("saisir cts : "))
b = float(a/2)
c = round (a/2)
if b>c:
    print(round (b), " pièces de 2 centimes & 1 pèces de 1 centimes")
elif b==c:
    print (round (b), " pièces de 2")
