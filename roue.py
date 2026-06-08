print("Bienvenue dans la roue")
from random import *
nom = ["Alex", "Sam", "Charlie"]

choix = ' '
def choix_ordinateur():
    nom = randint(1, 3)
    if nom == 1:
        ordi = "Alex"
    elif nom == 2:
        ordi = "Sam"
    else:
        ordi = "Charlie"
    return(ordi)

b = choix_ordinateur()
print(b)