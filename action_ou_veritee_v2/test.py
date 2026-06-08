from random import choice
import json

#variables
users = []
action = []
veritee = []
gage = []
action_path = r""
veritee_path = r""
gage_path = r""

def save_settings(liste, path):
    menu_save = input("1 : Ajouter des 'actions' (phrase)\n2 : Supprimer une 'action'\n3 : supprimer la sauvegarde\n: ")
    if menu_save == '1':
        while True:
            liste.append(input(" Entrer une 'action' (phrase), 's' pour terminer\n : "))
            print(f"L'élément {liste[-1]} a bien été ajouté à la liste.")
            if liste[-1] == 's':
                liste.remove('s')
                break
            with open(path, "w") as f:
                json.dump(liste, f)

    elif menu_save == '2':
        count(liste, "elements")
        while True:
            rm = input("(pour quitter ecrivez 'q')\nEntrer la phrase de la 'liste' à retirer\n : ")
            if rm not in liste:

                print(f"L'élément {rm} n'est pas dans 'action''.")
                pass
            elif rm == 'q':
                break
            else:
                liste.remove(rm)
                with open(path, "w") as f:
                    json.dump(liste, f)
                print(f"L'élément {rm} a bien été supprimé de la liste.")

    elif menu_save == '3':
        while True:
            menu_confirmation = input("ETES VOUS SUR DE VOULOIR SUPPRIMER DEFINITIVEMENT LA SAUVEGARGE ?\nO : oui\nN : non\n: ")
            if menu_confirmation == 'O':
                liste.clear()
                print("sauvegarde supprimer !")
            elif menu_confirmation == 'N':
                break
            else:
                print("erreur de saisi")
                pass

    else:
        print("erreur de saisi")
        pass

def load_choice_difficulty():
    # choice save for difficulty
    while True:
        menu_choice = input("n : normal\nd : difficile\nh : hard (alcool...)\nS : +18 (sex, soft)\nH : +18 (sex, hard)\nc : custom\n: ")
        if menu_choice == 'n':
            action_path = r"E:\Python\action_ou_veritee_v2\normal_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\normal_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\normal_gages.json"
            break
        elif menu_choice == 'd':
            action_path = r"E:\Python\action_ou_veritee_v2\difficile_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\difficile_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\difficile_gages.json"
            break
        elif menu_choice == 'h':
            action_path = r"E:\Python\action_ou_veritee_v2\hard_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\hard_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\hard_gages.json"
            break
        elif menu_choice == 'S':
            action_path = r"E:\Python\action_ou_veritee_v2\18soft_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\18soft_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\18soft_gages.json"
            break
        elif menu_choice == 'H':
            action_path = r"E:\Python\action_ou_veritee_v2\18hard_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\18hard_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\18hard_gages.json"
            break
        elif menu_choice == 'c':
            action_path = r"E:\Python\action_ou_veritee_v2\custom_actions.json"
            veritee_path = r"E:\Python\action_ou_veritee_v2\custom_veritees.json"
            gage_path = r"E:\Python\action_ou_veritee_v2\custom_gages.json"
            break
        else:
            print("erreur de saisie")
            pass

    # load save
    with open(action_path, "r") as a:
        action = json.load(a)

    with open(veritee_path, "r") as v:
        veritee = json.load(v)

    with open(gage_path, "r") as g:
        gage = json.load(g)

        list_saves = [action, veritee, gage, action_path, veritee_path, gage_path]
        return list_saves

def difficulty():
    print("\nDifficulte actions :")
    action.extend(load_choice_difficulty()[0])
    print("\n\nDifficulte veritee :")
    veritee.extend(load_choice_difficulty()[1])
    print("\n\nDifficulte gage :")
    gage.extend(load_choice_difficulty()[2])
    print("\n\n")
    look_saves()

def look_saves():
    print("\n//////////:  SAUVEGARDE CHARGE ://////////")
    count(action, "actions")
    count(veritee, "veritees")
    count(gage, "gages")
    print("\n//////////////////////////////////////////\n")

def count(str, string):
    print(f"\n     Liste des {string} :")
    count = 0
    for i in str:
        count += 1
        print(f"{count}. {i}")

def new_users(users):
    users.clear()
    while True:
        users.append(input(" Entree les noms des joueurs, terminer par 'q' pour finir\n : "))
        print(users)
        if users[-1] == 'q':
            users.remove('q')
            count(users, "joueurs")
            break

def gage_or_not(select_user):
    #gage or not
    while True:
        gage_or_not = input(" g : gage\n s : skip\n ")
        if gage_or_not == 'g':
            print(f"{select_user}, GAGE!!!" + choice(gage))
            break
        elif gage_or_not == 's':
            print("Bien jouer\n")
            break
        else:
            print("erreur de saisie")
            pass

#menu
while True:
    menu = input("\n\n1 : Difficule\n2 : save settings\n3 : Joueur\n4 : Jouer\nq : quitter\n: ")

    #difficulty
    if menu == '1':
        difficulty()

    #save settings
    elif menu == '2':
        while True:
            difficulty()
            print(action)
            print(veritee)
            print(gage)
            print(action_path)
            print(veritee_path)
            print(gage_path)
            while True:
                menu = input("1 : action\n2 : veritee\n3 : gage\n: ")
                if menu == '1':
                    save_settings(action, action_path)
                elif menu == '2':
                    save_settings(veritee, veritee_path)
                elif menu == '3':
                    save_settings(gage, gage_path)
                else:
                    print("erreur de saisi")
                    pass

    #users
    elif menu == '3':
        new_users(users)
        print(users)

    #game
    elif menu == '4':
        #new users
        if not users:
            new_users(users)

        if not action:
            difficulty()

        else:
            print("")

        #action or verity
        exit = "continue"
        print("BON JEU ^^\n(Remarque pour quitter ecrivez 'q')\n")
        while True:
            if exit == "stop":
                break

            while True:
                select_user = choice(users)

                choice_user = input(f"\n\n{select_user}, action ou veritee ? (a/v) : ")
                if choice_user == 'a':
                    print("\nAction :\n" + choice(action))
                    gage_or_not(select_user)
                    break
                elif choice_user == 'v':
                    print("\nVeritee :\n" + choice(veritee))
                    gage_or_not(select_user)
                    break
                elif choice_user == "q":
                    exit = "q"
                    break
                else:
                    print("erreur de saisie")
                    pass

    #exit
    elif menu == 'q':
        print("Merci d'avoir jouer ^^")
        break

    #error
    else:
        print("erreur de saisie")
        pass
