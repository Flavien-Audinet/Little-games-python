from random import randint

user_life = 50
ennemi_life = 50
potion = 3
tour = "user"

while True:
    potion_life = randint(15, 50)
    user_attack = randint(5, 10)
    ennemi_attack = randint(5, 15)

    if tour == "user":
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if choice == "1":
            ennemi_life -= user_attack
            print(f"Vous avez infligé {user_attack} points de dégats à l'ennemi ⚔")
            if ennemi_life <= 0:
                print("Tu as gagné 💪\nFin du jeu.")
                break
        elif choice == "2":
            if potion > 0:
                if user_life == 50:
                    print("Vous avez tous vos points de vie.")
                    continue
                else:
                    tour = "ennemi"
                    potion -= 1
                    user_life += potion_life
                    print(f"Vous récupérez {potion_life} points de vie ❤({potion} 🧪 restantes)")
                    if user_life > 50:
                        user_life = 50
            else:
                print("Vous n'avez plus de potion...")
                continue

        else:
            continue
        user_life -= ennemi_attack
        print(f"l'ennemi vous a infligé {ennemi_attack} points de dégats ⚔")
    elif tour == "ennemi":
        print("Vous passez votre tour...")
        user_life -= ennemi_attack
        print(f"l'ennemi vous a infligé {ennemi_attack} points de dégats ⚔")
        tour = "user"
    if user_life <= 0:
        print("Tu as perdu 💔\nFin du jeu.")
        break

    print(f"Il vous reste {user_life} points de vie.")
    print(f"Il reste {ennemi_life} points de vie à l'ennemi.")
    print("----------------------------------------------------------")
