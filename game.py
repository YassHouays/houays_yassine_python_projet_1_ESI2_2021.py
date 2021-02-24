#intialisation des variables création des joueurs
# un allié un ennemi 50 pts de vie chacun
# définir 3 potions utilisable par l'allié
# ennemi 0 potions
# une potion = récupération de vie aléatoire entre 15 et 50
# attaque = dégats aléatoire entre 5 et 10 
# utiliser une potion fait passer le prochain tour

import random
import time
class Player():
    def __init__(self, name):
        self.health = 50
        self.name = name
        self.wins = 0
        self.potion = 3

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} s'est fait détruire par {1}, avec {2} points de surplus!".format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} est mort de {1}!".format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("\n----------------------------\n{0} prends {1} points de dégats de {2}!".format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 50):
            self.health = 50
            self.potion -=1
            print("{0} s'est entièrement regénéré! il lui reste {1} potion(s)".format(self.name.capitalize(),self.potion))
        else:
            self.health += heal_amount
            self.potion -=1
            print("{0} se soigne de {1} points de vie! il lui reste {2} potion(s)".format(self.name.capitalize(), heal_amount, self.potion))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Choisissez une attaque: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("Erreur veuillez reessayer.")


def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....L'ennemi prépare son coup....")
    time.sleep(sleep_time)

    if (health <= 15):
        # Have the computer heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 2
        else:
            return 1
    elif (health == 50):
        return 1
    else:
        return 1


def play_round(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        # swap les joueurs un coup lordi un coup le joueur
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "Vous avez \033[96m{0}\033[0m points de vie restant et "
            "l'ennemi a \033[91m{1}\033[0m points de vie."
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("Attaque disponible:")
            print("1) Attaque - Faites des dégats à l'ennemi.")
            print("2) Potion - Restaure votre vie")
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1):
            damage = random.randrange(5, 10)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            heal = random.randrange(15, 50)
            if (human.potion > 0):
                current_player.calculate_heal(heal)
            else:
                print ("Plus de potions")
                current_player = computer
        else:
            print ("Erreur veuillez rééssayer")

        if (human.health == 0):
            print("Vous avez perdu")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("Félicitations vous avez gagné")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("Bienvenu dans le 1V1 le plus cool")

    computer = Player("L'ennemi")

    name = input("Entrer votre pseudo \033[1m")
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):
        print("Score:")
        print("Vous - {0}".format(human.wins))
        print("L'ennemi - {0}".format(computer.wins))

        computer.health = 50
        human.health = 50
        play_round(computer, human)
        print()
        response = input("Rejouer?(Y/N)")
        if (response.lower() == "n"):
            break

start_game()