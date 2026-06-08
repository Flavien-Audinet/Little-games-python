from random import *
print("\n              Bienvenue au Pierre, Feuille, Ciseaux")
joueur1 = input("\nQuel est votre nom ? : \n   ")
n_ordi = input("\nQuel est le nom de l'ordinateur ? : \n   ")

def choix_utilisateur():
    joueur = input("\nPierre\nFeuille\nCiseaux\n\n   ")
    while joueur not in ["pierre", "feuille", "ciseaux"]:
        joueur = input("\npierre\nfeuille\nciseaux\n\n   ")
    return(joueur)

def choix_ordinateur():
    n = randint(1, 3)
    if n == 1:
        ordi = "   pierre"
    elif n == 2:
        ordi = "   feuille"
    else:
        ordi = "   ciseaux"
    return(ordi)

a = choix_utilisateur()
b = choix_ordinateur()
print(b)

###################################################################
if a == "pierre" and b == "   ciseaux":
    print(f"\n{joueur1} a gagne(e).\n{n_ordi} a perdu.")

elif a == "pierre" and b == "   feuille":
    print(f"\n{n_ordi} a gagne(e).\n{joueur1} a perdu.")

elif a == "pierre" and b == "   pierre":
    print("\nEgalite.")

###################################################################
if a == "feuille" and b == "   pierre":
    print(f"\n{joueur1} a gagne(e).\n{n_ordi} a perdu.")

elif a == "feuille" and b == "   ciseaux":
    print(f"\n{n_ordi} a gagne(e).\n{joueur1} a perdu.")

elif a == "feuille" and b == "   feuille":
    print("\nEgalite.")

###################################################################
if a == "ciseaux" and b == "   feuille":
    print(f"\n{joueur1} a gagne(e).\n{n_ordi} a perdu.")

elif a == "ciseaux" and b == "   pierre":
    print(f"\n{n_ordi} a gagne(e).\n{joueur1} a perdu.")

elif a == "ciseaux" and b == "   ciseaux":
    print("\nEgalite.")