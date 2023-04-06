import random
import time
from character import leveling
from combat import game_combat, afflictions


def guessing_game(current_character: dict) -> None:
    """
    Initialize a number guessing mini-game for the user to play.

    :param current_character: a dictionary containing 'HP' as a key
    :precondition: current_character 'HP' key value must be a positive integer more than 0
    :postcondition: modifies 'HP' key value in current_character and print a prompt as a side effect
    """
    secret_number = str(random.randint(1, 5))
    print("AHAHAHAHAHHAHA CAN'T ESCAPE RNG.")
    guess = input("Enter a number between 1 and 5 inclusive: ")
    if guess == secret_number:
        print("THAT WAS A LUCKY GUESS PUNK")
    elif not guess.isdigit():
        current_character['HP'] -= 10
        print(f"Seriously, that isn't even a number. Take some damage. HP is now at {current_character['HP']}")
    else:
        current_character['HP'] -= 10
        print(f"WRONG. DAMAGE TAKEN. Number was {secret_number}. HP is now at {current_character['HP']}")


def engage_combat(character, creep):
    determine_first_engage(character=character, creep=creep)
    while character['HP'] > 0 and creep['HP'] > 0 and character['Affliction'] != 'Coward':
        afflictions.check_for_creep_afflictions(creep=creep, character=character)
        check_for_turn(character, creep)
    if character['Affliction'] == 'Coward':
        guessing_game(current_character=character)
        return
    if check_for_victory(character, creep):
        encounter_victory(character, creep)


def check_for_turn(character, creep):
    if character['Turn']:
        game_combat.character_attack(character=character, creep=creep)
    else:
        game_combat.creep_attack(character=character, creep=creep)


def determine_first_engage(character, creep):
    if random.randint(1, 2) == 1:
        character['Turn'] = True
    else:
        creep['Turn'] = True


def spawn_monster():
    slime = {'Name': 'Slime', 'HP': 50, 'ATK': 10, 'Affliction': None, 'EXP': 5}
    bigger_slime = {'Name': 'Slime\'s bigger brother', 'HP': 60, 'ATK': 15, 'Affliction': None, 'EXP': 10,
                    'Turn': False}
    zombie = {'Name': 'Zombie', 'HP': 75, 'ATK': 25, 'Affliction': None, 'EXP': 15, 'Turn': False}
    wormie = {'Name': 'Worm', 'HP': 20, 'ATK': 5, 'Affliction': None, 'EXP': 10, 'Turn': False}
    alaskan_bullworm = {'Name': 'THE ALASKAN BULLWORM', 'HP': 75, 'ATK': 30, 'Affliction': None, 'EXP': 30,
                        'Turn': False}
    mob_spawner = (slime, bigger_slime, zombie, wormie, alaskan_bullworm)
    return mob_spawner[random.randint(0, len(mob_spawner)-1)]


def decide_encounter(character):
    encounter = random.choices([engage_combat, guessing_game])
    if engage_combat in encounter:
        return engage_combat(character, spawn_monster())
    else:
        return guessing_game(character)


def check_for_victory(character, creep):
    if character['HP'] > 0 >= creep['HP']:
        return True
    else:
        return False


def encounter_victory(character, creep):
    if character['HP'] > 0 >= creep['HP']:
        leveling.gain_experience(current_char=character, creep=creep)
        leveling.level_up(current_char=character)
        character['HP'] += 20
        # character['HP'] += creep['EXP']
        character['MP'] += 30
    time.sleep(3)
    print(f"You have healed for 20 HP.")
    print(f"You have regenerated 30 mana.")
    print(f"You have slain {creep['Name']}!")
    time.sleep(3)


def defeat():
    pass


def spawn_boss(character):
    floor_one_boss = {'Name': 'EYE OF CTHULHU', 'HP': 1, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100} # 150
    floor_two_boss = {'Name': 'MIMIC', 'HP': 1, 'ATK': 50, 'Affliction': None, 'Turn': False,
                      'EXP': 200} # 300
    floor_three_boss = {'Name': 'ZAKUM', 'HP': 1, 'ATK': 75, 'Affliction': None, 'Turn': False,
                        'EXP': 300} # 500
    if character['X-coord'] == 4 and character['Y-coord'] == 4 and character['Z-coord'] == 0:
        return floor_one_boss
    elif character['X-coord'] == 4 and character['Y-coord'] == 4 and character['Z-coord'] == 1:
        return floor_two_boss
    else:
        return floor_three_boss


def main():
    """

    :return:
    """


if __name__ == "__main__":
    main()
