voyelle=("aeiouyAEIOUY")
consonnes=("bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ")

lettre = input("veuillez taper une lettre : ")

for i in range (len(voyelle)):
    pass
    

if lettre in voyelle:
    print("vous avez saisie une voyelle")

    if lettre in "aeiouy":
        print ("qui est en minuscule.")
    else:
        print("qui est en MAJUSCULE")

    
elif lettre in consonnes:
    print("vous avez saisie une consonne")

    if lettre in ("bcdfghjklmnpqrstvwxz"):
        print("qui est en minuscule")
    else:
        print("qui est en MAJUSCULE")
