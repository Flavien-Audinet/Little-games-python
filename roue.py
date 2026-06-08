print("Bienvenue dans la roue")
from random import *
nom = ["Flavien", "Meïssane", "Bebew"]

choix = ' '
def choix_ordinateur():
    nom = randint(1, 3)
    if nom == 1:
        ordi = "Flavien"
    elif nom == 2:
        ordi = "Meïssane"
    else:
        ordi = "Bebew"
    return(ordi)

b = choix_ordinateur()
print(b)