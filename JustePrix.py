print("Bienvenue au juste prix ! \n")

while True:
    switch_1 = 0
    switch_1 = input(" J : Jouer \n R : Règles \n Q : Quitter \n")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if switch_1 != 'r' 'q' :
            print(" ")

            if switch_1 == 'j' :
                switch_2 = 0
                switch_2 = input("   F : Facile \n   N : Normal \n   D : Difficile \n   H : HARD CORE \n")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                if switch_2 == 'f' :
                    import random
                    choix = random.randint(0, 100)
                    nb_tentative = 0
                    nb_tentative += 1

                    while True:
                        reponse = int(input("\nDeviner le nombre :\n "))

                        if choix != reponse :

                            if reponse < choix :
                                print("C'est plus grand \n")
                            else :
                                print("C'est plus petit \n")

                            if reponse > 100 :
                                print("Le maximum c'est 100")
                                nb_tentative -= 1

                        else :
                            break
                    print("Bravo !")
                    print(f"Votre nombre de tentatives : {nb_tentative} \n")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                elif switch_2 == 'n' :
                    import random
                    choix = random.randint(0, 1000)
                    nb_tentative = 0
                    nb_tentative += 1

                    while True:
                        reponse = int(input("Deviner le nombre : \n"))

                        if choix != reponse :

                            if reponse < choix :
                                print("C'est plus grand")
                            else :
                                print("C'est plus petit")

                            if reponse > 1000 :
                                print("Le maximum c'est 1 000")
                                nb_tentative -= 1

                        else :
                            break
                    print("Bravo !")
                    print(f"Votre nombre de tentatives : {nb_tentative}")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                elif switch_2 == 'd' :
                    import random
                    choix = random.randint(0, 10000)
                    nb_tentative = 0
                    nb_tentative += 1

                    while True:
                        reponse = int(input("Deviner le nombre : \n"))

                        if choix != reponse :

                            if reponse < choix :
                                print("C'est plus grand")
                            else :
                                print("C'est plus petit")

                            if reponse > 10000 :
                                print("Le maximum c'est 10 000")
                                nb_tentative -= 1

                        else :
                            break
                    print("Bravo !")
                    print(f"Votre nombre de tentatives : {nb_tentative}")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                elif switch_2 == 'h' :
                    import random
                    choix = random.randint(0, 10000000)
                    nb_tentative = 0
                    nb_tentative += 1

                    while True:
                        reponse = int(input("Deviner le nombre : \n"))

                        if choix != reponse :

                            if reponse < choix :
                                print("C'est plus grand")
                            else :
                                print("C'est plus petit")

                            if reponse > 10000000 :
                                print("Le maximum c'est 10 000 000")
                                nb_tentative -= 1

                        else :
                            break
                    print("Bravo !")
                    print(f"Votre nombre de tentatives : {nb_tentative}")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                elif switch_2 == 'q' :
                    print("Vous avez quittez !")
                    break

                elif switch_2 != 'f' 'n' 'd' 'h' 'q':
                    print("erreur de saisie")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            elif switch_1 == 'r' :
                print("Les règles sont très simple il suffit de trouver le nombre Mystère .")
                print("    En facile le nombre est entre 0 et 100")
                print("    En normal le nombre est entre 0 et 1 000")
                print("       En difficile le nombre est entre 0 et 10 000")
                print("       En HARD CORE le nombre est entre 0 et 10 000 000")
                print(" ")
                print("    Bonne Chance !\n")

            elif switch_1 == 'q' :
                print("Vous avez quittez le jeu!")
                break