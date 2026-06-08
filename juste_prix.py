import random

print("Bienvenue au Juste Prix\n")
nb_mystere = random.randint(0, 100)

while True:
    joueur = input("Entrer un nombre entre 0 et 100 : ")
    joueur = int(joueur)
    if joueur == nb_mystere:
        print("Bravo")
        break
    elif joueur < nb_mystere:
        print("C'est plus grand")
    else:
        print("C'est plus petit")
