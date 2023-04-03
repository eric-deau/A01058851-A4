import random


def guessing_game(current_character: dict) -> None:
    """
    Initialize a number guessing mini-game for the user to play.

    :param current_character: a dictionary containing keys 'X-coordinates', 'Y-coordinates', and 'HP'
    :precondition: current_character 'HP' key value must be a positive integer more than 0
    :postcondition: modifies 'HP' key value in current_character and print a prompt as a side effect
    """
    secret_number = str(random.randint(1, 5))
    print("AN ENEMY! TIME TO FIGHT FOR YOUR LIFE")
    guess = input("Enter a number between 1 and 5 inclusive: ")
    if guess == secret_number:
        print("ENEMY IS DEFEATED")
    elif not guess.isdigit():
        current_character['HP'] -= 1
        print(f"Seriously, that isn't even a number. Take some damage. HP is now at {current_character['HP']}")
    else:
        current_character['HP'] -= 1
        print(f"WRONG. DAMAGE TAKEN. Number was {secret_number}. HP is now at {current_character['HP']}")


def spawn_monster():
    slime = {'Name': 'Slime', 'HP': 50, 'ATK': 10, 'Affliction': None, 'EXP': 5}
    bigger_slime = {'Name': 'Slime\'s bigger brother', 'HP': 60, 'ATK': 15, 'Affliction': None, 'EXP': 10}
    zombie = {'Name': 'Zombie', 'HP': 75, 'ATK': 25, 'Affliction': None, 'EXP': 15}
    wormie = {'Name': 'Worm', 'HP': 1, 'ATK': 5, 'Affliction': None, 'EXP': 10}
    alaskan_bullworm = {'Name': 'THE ALASKAN BULLWORM', 'HP': 75, 'ATK': 30, 'Affliction': None, 'EXP': 30}
    mob_spawner = (slime, bigger_slime, zombie, wormie, alaskan_bullworm)
    return mob_spawner[random.randint(0, len(mob_spawner)-1)]


def main():
    print(spawn_monster())


if __name__ == "__main__":
    main()
