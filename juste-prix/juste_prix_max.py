import random
print("Bienvenue au JUSTE PRIX")

nb = int(input("choisir la valeur MAX:  "))
nb_alea = random.randint(1, nb)
print(nb_alea)
nb_tentative = 0

while True:
    user = int(input("___________________\nEntrer un nombre\n"))
    nb_tentative += 1
    if user != nb_alea:

        if user < nb_alea:
            print("C'est plus grand !")
        else:
            print("C'est plus petit !")

        if user > nb:
            print(f"Le maximum est {nb}")
            nb_tentative -= 1
    else:
        print(f"///////////////////\nBravo!!!\nVotre nombre de tentatives: {nb_tentative}")
        break
