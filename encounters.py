import random
import combat


def check_for_foes() -> int:
    """
    Determine if a character will have an encounter in the playing board 25% of the time.

    :postcondition: determines if a mini-game will be initialized 25% of the time
    :return: a boolean value representing if a foe is encountered 25% of the time
    """
    return random.randint(1, 4) == 1


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


def engage_combat(character, creep):
    if random.randint(1, 2) == 1:
        character['Turn'] = True
    else:
        creep['Turn'] = True
    while character['HP'] != 0 or creep['HP'] != 0:
        if character['Turn']:
            combat.character_attack(character, creep)
        else:
            combat.creep_attack(character, creep)


def spawn_monster():
    slime = {'Name': 'Slime', 'HP': 50, 'ATK': 10, 'Affliction': None, 'EXP': 5}
    bigger_slime = {'Name': 'Slime\'s bigger brother', 'HP': 60, 'ATK': 15, 'Affliction': None, 'EXP': 10,
                    'Turn': False}
    zombie = {'Name': 'Zombie', 'HP': 75, 'ATK': 25, 'Affliction': None, 'EXP': 15, 'Turn': False}
    wormie = {'Name': 'Worm', 'HP': 1, 'ATK': 5, 'Affliction': None, 'EXP': 10, 'Turn': False}
    alaskan_bullworm = {'Name': 'THE ALASKAN BULLWORM', 'HP': 75, 'ATK': 30, 'Affliction': None, 'EXP': 30,
                        'Turn': False}
    mob_spawner = (slime, bigger_slime, zombie, wormie, alaskan_bullworm)
    return mob_spawner[random.randint(0, len(mob_spawner)-1)]


def spawn_boss(character):
    floor_one_boss = {'Name': 'EYE OF CTHULHU', 'Level': 2, 'HP': 200, 'ATK': 50, 'Affliction': None, 'Turn': False}
    floor_two_boss = {'Name': 'MIMIC', 'Level': 3, 'HP': 300, 'ATK': 100, 'Affliction': None, 'Turn': False}
    floor_three_boss = {'Name': 'ZAKUM', 'Level': 4, 'HP': 500, 'ATK': 200, 'Affliction': None, 'Turn': False}
    if character['X-coords'] == 4 and character['Y-coords'] == 4 and character['Z-coords'] == 0:
        return floor_one_boss
    elif character['X-coords'] == 4 and character['Y-coords'] == 4 and character['Z-coords'] == 1:
        return floor_two_boss
    else:
        return floor_three_boss


def main():
    print(spawn_monster())


if __name__ == "__main__":
    main()
