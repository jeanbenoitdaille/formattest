

texte = "Bonjour Udemy"
longueur = len(texte)
     
symbole1 = "-"
symbole2 = "|"
     
print(symbole1*longueur)
     
for lettre in texte:
        print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))
     
print(symbole1*longueur)