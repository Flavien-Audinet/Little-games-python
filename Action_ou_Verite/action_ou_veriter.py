import random

print("Bienvenue a L'ACTION OU VERITE")
menu = input("  Choix Du Theme de l'action ou verite\n    1 : Facile\n    2 : Normal\n    3 : Difficile\n    4 : Soiree(alcool)\n")

while True:
    if menu == '1':
        joueur = []
        while True:
            joueur.append(input("Entrer les pseudos des joueurs (finir par s): "))
            print(joueur)
            if joueur[-1] == 's':
                joueur.remove('s')
                print(joueur)
                print("\n\n")
                break

        action = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']
        a1 = "Marche a quatre pattes pendant 10 seconde"
        a2 = "Crie de toute tes force"
        a3 = "Coure pendant 10 seconde"
        a4 = "Fais des bruit d'animaux"
        a5 = "Tourne 10 fois sur toi meme "
        a6 = "Dis a une personne que tu l'aime(n'importe qui)"
        a7 = "Fais 3 squates"
        a8 = "Crie je suis un garcon (pour les filles) ou une fille (pour les garcons)"
        a9 = "Passe ton bras gauche sous ta jambe droite en touchant ton nez avec ta main gauche"
        a10 = "Ressite l'alphabet a lenvers"

        verite = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15']
        v1 = "Dis ton second prenom"
        v2 = "Sur qui tu crush"
        v3 = "Jusqu'a quel age as tu fais pipi au lit"
        v4 = "Racconte ton pire malaise"
        v5 = "A tu deja embrassez quelqu'un"
        v6 = "Qui est la personne que tu deteste (ecole ou autre)"
        v7 = "As tu deja pleurer car tu n'arrivais pas a faire caca"
        v8 = "As tu deja pleurer pour quelqu'un"
        v9 = "A quel point aime tu ton crush"
        v10 = "As tu deja ris du malheure de quelqu'un"
        v11 = "Quand as tu pete et accuse quelqu'un d'autre pour la derniere fois"
        v12 = "Quelle etais la derniere fois ou tu as ete hyper radin(e)"
        v13 = "Parmi les gens dans cette piece, de qui as tu deja reve"
        v14 = "Quelle partie du corps de la personne a ta droite apprecies tu le plus"
        v15 = "t'es tu deja baigne a poil dans la mer"

        gage = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10']
        g1 = "Fais 5 pompes"
        g2 = "Fais 5 squates"
        g3 = "Dis a une personne que t'aime bien que tu la deteste"
        g4 = "Prete ton telephone pendant 10 seconde deverouille"
        g5 = "Coure pendant 20 secondes"
        g6 = "Prete ton telephone pendant 30 seonde deverouille"
        g7 = "Fais 10 pompes"
        g8 = "Fais 10 squates"
        g9 = "Fais un calin a la personne que tu desteste"
        g10 = "Fais un massage a la personne que tu deteste"

        while True:
            choix_joueur = random.choice(joueur)
            print(choix_joueur)

            choix = input("Action ou Verite (a ou v): ")
            if choix == "a":
                print("action")
                choix_action = random.choice(action)
                if choix_action == 'a1':
                    print(a1)
                elif choix_action == 'a2':
                    print(a2)
                elif choix_action == 'a3':
                    print(a3)
                elif choix_action == 'a4':
                    print(a4)
                elif choix_action == 'a5':
                    print(a5)
                elif choix_action == 'a6':
                    print(a6)
                elif choix_action == 'a7':
                    print(a7)
                elif choix_action == 'a8':
                    print(a8)
                elif choix_action == 'a9':
                    print(a9)
                else :
                    print(a10)

            elif choix == "v":
                print("verite")
                choix_verite = random.choice(verite)
                if choix_verite == 'v1':
                    print(v1)
                elif choix_verite == 'v2':
                    print(v2)
                elif choix_verite == 'v3':
                    print(v3)
                elif choix_verite == 'v4':
                    print(v4)
                elif choix_verite == 'v5':
                    print(v5)
                elif choix_verite == 'v6':
                    print(v6)
                elif choix_verite == 'v7':
                    print(v7)
                elif choix_verite == 'v8':
                    print(v8)
                elif choix_verite == 'v9':
                    print(v9)
                elif choix_verite == 'v10':
                    print(v10)
                elif choix_verite == 'v11':
                    print(v11)
                elif choix_verite == 'v12':
                    print(v12)
                elif choix_verite == 'v13':
                    print(v13)
                elif choix_verite == 'v14':
                    print(v14)
                else :
                    print(v15)

            else :
                print("erreur")

            choix_1 = input("\nGage oui ou non (o ou n): ")
            if choix_1 == 'o':
                choix_gage = random.choice(gage)
                if choix_gage == 'g1':
                    print(g1)
                    print("\n\n")
                elif choix_gage == 'g2':
                    print(g2)
                    print("\n\n")
                elif choix_gage == 'g3':
                    print(g3)
                    print("\n\n")
                elif choix_gage == 'g4':
                    print(g4)
                    print("\n\n")
                elif choix_gage == 'g5':
                    print(g5)
                    print("\n\n")
                elif choix_gage == 'g6':
                    print(g6)
                    print("\n\n")
                elif choix_gage == 'g7':
                    print(g7)
                    print("\n\n")
                elif choix_gage == 'g8':
                    print(g8)
                    print("\n\n")
                elif choix_gage == 'g9':
                    print(g9)
                    print("\n\n")
                else :
                    print(g10)
                    print("\n\n")
            else:
                print("\n\n")
