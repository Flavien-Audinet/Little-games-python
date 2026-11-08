#######################################################################################################################
#normal
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
#difficile
#soiree(alcool)
#-18(soft)
#-18(HARD)
#######################################################################################################################
#normal
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
#difficile
#soiree(alcool)
#-18(soft)
#-18(HARD)
#######################################################################################################################
#normal
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
#difficile
#soiree(alcool)
#-18(soft)
#-18(HARD)
#######################################################################################################################
import random

print("Bienvenue a Action ou Verite\n")
menu = input("1: Normal\n2: Difficile\n3: Soirée(alcool)\n4: -18(soft)\n5: -18(HARD)\n")

while True:
    if menu == '1':
        joueur = []
        while True:
            joueur.append(input("Entrer les pseudos des joueurs (finir par s):\n"))
            print(joueur)
            if joueur[-1] == 's':
                joueur.remove('s')
                print(joueur)
                break

        print("\n######################################################################################\n")

        action = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
        verite = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]
        gage = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]

        while True:
            selection_joueurs = random.choice(joueur)
            print(selection_joueurs)

            choix_joueur = input("Action ou Verite (a ou v): ")
            if choix_joueur == 'a':
                print("Action")
                selection_action = random.choice(action)
                print(selection_action)

            elif choix_joueur == 'v':
                print("Vérité")
                selection_verite = random.choice(verite)
                print(selection_verite)
            else:
                print("erreur de saisie")

            choix_gage = input("\nGage : oui ou non (o ou n): ")
            if choix_gage == 'o':
                print("\nGAGE")
                selection_gage = random.choice(gage)
                print(selection_gage)
                print("\n######################################################################################\n")
            elif choix_gage == 'n':
                print("\n######################################################################################\n")
            else:
                print("erreur de saisie")
                print("\n######################################################################################\n")
#######################################################################################################################
