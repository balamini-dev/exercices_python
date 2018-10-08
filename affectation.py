# Exercice 1 : Ecrire programme qui calcule le double d’un entier
# Prog double // E: x : entier  S: double : entier
n = int(input('n ? : '))
double = n * 2
print("double : ",double)

# Exercice 2 : Ecrire programme qui calcule le carré d’un réel.
# Prog carre // E: x : réel  S: carreX : reel
x = float(input('x ? : '))
carreX = x * x
print("carreX : ",carreX)

# Exercice 3 : Ecrire un programme qui transforme des degrés Fahrenheit en degrés Celsius sachant que :
# Prog fahr // E: fahr : réel S: celsius : reel
# 0° C correspond à 32 °F et que 100 °C égale 212 °F.
fahr = float(input('entrez une temperature en Fahrenheit : '))
celsius = (fahr-32)*5/9 + 32
print("celsius : %.2f" % (celsius))

# Exercice 4 : Ecrire un programme qui calcule le prix TTC (toutes taxes comprises) sachant que :
# le prix TTC, c’est le prix HT (hors taxes) auquel on ajoute la TVA. Il existe 4 valeurs de TVA : 20%, 10%, 5,5% et 2,1%.
# Prog prixTTC // E: prixHT : réel - tva : réel  S: prixTTC : reel
prixHT = float(input('prixHT ? : '))
tva = float(input('TVA parmi 20%, 10%, 5.5% ou 2.1%? : '))
prixTTC = prixHT+ prixHT*tva/100
print("prixTTC : ",prixTTC)

# Exercice 5 : Ecrire un programme qui calcule la circonférence d’un cercle et l'aire du disque délimité par ce cercle.
# Prog cercle // E: rayon : réel  S: circonference : reel - aire : réel
from math import *
rayon = float(input('rayon ? : '))
circonference = 2 * pi * rayon
aire =  pi * rayon * rayon
print("circonference : ",round(circonference,2))
print("aire : ",round(aire,2))

# Exercice 6 : Trouvez ce que fait le programme suivant 
# Prog exo6 
a = int(input('a ? : '))
b = int(input('b ? : '))
a=b-a
b=b-a
a=a+b
print("a : ",a, " - b : ", b)
 
# Exercice 7 : Trouvez ce que fait le programme suivant 
# Prog exo7
a = int(input('a ? : '))
b = int(input('b ? : '))
c = int(input('c ? : '))
a=a+b+c
b=b+c
c=a-c
a=a-c;
b=c-b+a;
c=c-b;
print("a : ",a, " - b : ", b, " - c : ", c)