'''
Exercice 2 : année bissextile
Ecrire un programme qui affiche le nombre de jours d’un mois d’une année donnée. On rappelle
que les années bissextiles sont celles qui sont divisibles par 4. Toutefois, les années divisibles
par 100 ne sont pas bissextiles. Mais les années divisibles par 400 sont quand même bissextiles.
Par exemple : 2008 est bissextile, 2010 n’est pas bissextile, 2000 est bissextile, 1900 n’est pas
bissextile.

Pseudo code (algorithme)

si annee%4 !=0
	nbJours=28
sinonsi annee%100 !=0
	nbJours=29
sinonsi annee % 100 !=0
	nbJours=28
sinon
	nbJours=29
fin

'''
###################################

nbJours=0
annee=int(input('entrer une année : '))
if annee%4 !=0:
    nbJours=28
elif annee%100!=0:
    nbJours=29
elif annee % 100!=0:
    nbJours=28
else:
    nbJours=29
print (nbJours)
