import random
import time
import json
from character import leveling
from combat import game_combat, afflictions


def guessing_game(current_char: dict) -> None:
    """
    Initialize a number guessing mini-game for the user to play.

    :param current_char: a dictionary containing 'HP', 'MP' and 'Name' as a key
    :precondition: current_char 'Name', 'HP' and 'MP' key value must be a positive number more than 0
    :postcondition: modifies 'HP' and 'MP' key value in current_char
    """
    if type(current_char) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'HP' not in current_char:
        raise KeyError("'HP' must exist in dictionary as a key.")
    elif current_char['HP'] < 0:
        raise ValueError("HP must be a number more than 0.")
    else:
        print(f"Welcome to the funhouse, {current_char['Name']}..")
        time.sleep(2)
        secret_number = str(random.randint(1, 5))
        guess = input("Enter a number between 1 and 5 inclusive: ")
        if guess == secret_number:
            win_guessing_game(current_char=current_char)
        else:
            lose_guessing_game(current_char=current_char, guess=guess, secret_number=secret_number)


def lose_guessing_game(current_char: dict, guess: str, secret_number: str) -> None:
    """
    Decrement character's HP values by 10% for losing the guessing game.

    :param current_char: a dictionary with 'Affliction', 'Name' and 'HP' as keys
    :param guess: a string
    :param secret_number: a numeric character as a string
    :precondition: current_char must be a dictionary with 'Affliction', 'Name', 'HP', and 'MP' as keys
    :precondition: guess must be a string
    :precondition: secret_number must be a string containing a numeric character
    :postcondition: modifies current_char 'HP' key
    :raises: TypeError: if current_char is not a dictionary or guess and secret_number is not a string
    :raises: ValueError: if secret_number is not a numeric character

    >>> test_char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> test_secret_num = "5"
    >>> lose_guessing_game(test_char_one, "The guess that gods are disappointed with.", "3")
    The gods are disappointed with your answer. Lose 30.0 HP.
    >>> test_char_one['HP']
    270.0

    >>> test_char_two = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> test_secret_num = "5"
    >>> lose_guessing_game(test_char_two, "4", "5")
    The gods are pleased with your answer, but they are not on your side today. Correct number was 5. Lose 30.0 HP.
    >>> test_char_two['HP']
    270.0
    """
    if type(current_char) is not dict:
        raise TypeError("current_char must be a dictionary.")
    elif type(guess) is not str or type(secret_number) is not str:
        raise TypeError("guess and secret_number must be a string.")
    elif not secret_number.isdigit():
        raise ValueError("secret_number must be a numeric character.")
    else:
        if current_char['Affliction'] == 'Coward':
            print(f"You have committed sacrilege by running away from a fight, {current_char['Name']}")
        if not guess.isdigit():
            print(f"The gods are disappointed with your answer. Lose {current_char['HP']*0.1} HP.")
        else:
            print(f"The gods are pleased with your answer, but they are not on your side today."
                  f" Correct number was {secret_number}. Lose {current_char['HP']*0.1} HP.")
        current_char['HP'] -= current_char['HP'] * 0.1


def win_guessing_game(current_char: dict) -> None:
    """
    Increment a character's HP and MP by their own HP and MP plus 10%.

    :param current_char: a dictionary that has 'Name', 'HP' and 'MP' keys
    :precondition: current_char 'HP' and 'MP' must be more than 0
    :postcondition: modifies current_char 'HP' and 'MP' keys
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if current_char does not contain 'HP', 'MP', and 'Name' as keys
    :raises: ValueError: if current_char 'HP' and 'MP' values are less than zero

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> win_guessing_game(test_char_one)
    The gods have blessed you, RAKSHASA..
    You have healed for 30.0 HP.
    You have gained 20.0 MP.
    """
    if type(current_char) is not dict:
        raise TypeError("A dictionary must be passed.")
    elif 'HP' not in current_char or 'MP' not in current_char:
        raise KeyError("'Name', 'HP' and 'MP' must be keys in the dictionary.")
    elif current_char['HP'] < 0 or current_char['MP'] < 0:
        raise ValueError("Dictionary keys 'HP' and 'MP' must be more than or equal to 0.")
    else:
        print(f"The gods have blessed you, {current_char['Name']}..")
        time.sleep(2)
        print(f"You have healed for {current_char['HP'] * 0.1} HP.")
        print(f"You have gained {current_char['MP'] * 0.1} MP.")
        current_char['HP'] += current_char['HP'] * 0.1
        current_char['MP'] += current_char['MP'] * 0.1
        time.sleep(2)


def engage_combat(current_char: dict, creep: dict) -> None:
    """
    Dictate the occurring events in the battle between current_char and creep.

    :param current_char: a dictionary
    :param creep: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :precondition: creep must contain 'Name' as a key and a string as the value
    :precondition: creep must contain 'HP', 'ATK' and 'EXP' as keys with positive numbers as the value
    :precondition: creep must contain 'Affliction' as a key
    :precondition: creep must contain 'Turn' as a key and a boolean value as the value
    :postcondition: determines the events occurring in a fight between current_char and creep
    """
    print(f"YOU HAVE ENCOUNTERED {creep['Name']}!")
    time.sleep(2)
    determine_first_engage(current_char=current_char, creep=creep)
    while current_char['HP'] > 0 and creep['HP'] > 0 and current_char['Affliction'] != 'Coward':
        check_player_turn = check_for_turn(current_char)
        if check_player_turn:
            game_combat.character_attack(character=current_char, creep=creep)
        else:
            game_combat.creep_attack(character=current_char, creep=creep)
        afflictions.check_for_creep_afflictions(creep=creep)
    if current_char['Affliction'] == 'Coward':
        guessing_game(current_char=current_char)
        return
    if check_for_victory(current_char=current_char, creep=creep):
        encounter_victory(current_char=current_char, creep=creep)


def check_for_turn(current_char: dict) -> bool:
    """
    Determine the current turn in the engagement.

    :param current_char: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :postcondition: determines which entity can take an action in the fight
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if current_char does not contain 'Turn' as a key
    :raises: TypeError: if current_char 'Turn' key is not a boolean

    >>> test_char_one = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3, \
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> check_for_turn(test_char_one)
    False

    >>> test_char_two = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3, \
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True, \
                         'Affliction': None}
    >>> check_for_turn(test_char_two)
    True
    """
    if type(current_char) is not dict:
        raise TypeError("A dictionary must be passed as an argument.")
    elif 'Turn' not in current_char:
        raise KeyError("'Turn' must be a key in the dictionary.")
    elif type(current_char['Turn']) is not bool:
        raise TypeError("Dictionary key 'Turn' must be a boolean value.")
    else:
        return True if current_char['Turn'] else False


def determine_first_engage(current_char: dict, creep: dict) -> None:
    """
    Dictate the first turn in an engagement.

    :param current_char: a dictionary
    :param creep: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :precondition: creep must contain 'Name' as a key and a string as the value
    :precondition: creep must contain 'HP', 'ATK' and 'EXP' as keys with positive numbers as the value
    :precondition: creep must contain 'Affliction' as a key
    :precondition: creep must contain 'Turn' as a key and a boolean value as the value
    :postcondition: determines the events occurring in a fight between current_char and creep
    :raises: TypeError: if current_char or creep is not a dictionary
    :raises: KeyError: if current_char or creep does not contain 'Turn' as a key
    :raises: TypeError: if current_char or creep 'Turn' key is not a boolean
    """
    if type(current_char) is not dict or type(creep) is not dict:
        raise TypeError("A dictionary must be passed as an argument.")
    elif type(current_char['Turn']) is not bool or type(creep['Turn']) is not bool:
        raise TypeError("Dictionary key 'Turn' must be a boolean value.")
    elif 'Turn' not in current_char or 'Turn' not in creep:
        raise KeyError("'Turn' must be a key in the dictionary.")
    else:
        if random.randint(1, 2) == 1:
            current_char['Turn'] = True
        else:
            creep['Turn'] = True


def spawn_monster() -> dict:
    """
    Spawn a monster for the character to fight.

    :precondition: mobs.json must be a file existing in directory named combat
    :postcondition: determines the monster spawned
    :return: a dictionary representing a monster
    :raises: FileNotFoundError: if mobs.json does not exist in directory called combat
    """
    with open('combat/mobs.json', 'r') as file_object:
        list_of_mobs = json.load(file_object)
    mob = list_of_mobs[random.randint(0, len(list_of_mobs)-1)]
    mob['HP'] = random.randint(mob['HP'], mob['HP']+50)
    return mob


def decide_encounter() -> bool:
    """
    Determine the type of encounter the character will come across.

    :postcondition: dictates the encounter that will occur
    :return: a boolean value representing the type of encounter a character will engage in
    """
    encounter = [engage_combat, guessing_game]
    if engage_combat is encounter[random.randint(0, len(encounter)-1)]:
        return True
    else:
        return False


def check_for_victory(current_char: dict, creep: dict) -> bool:
    """
    Determine if a character has won an encounter or not.

    :param current_char: a dictionary
    :param creep: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :precondition: creep must contain 'Name' as a key and a string as the value
    :precondition: creep must contain 'HP', 'ATK' and 'EXP' as keys with positive numbers as the value
    :precondition: creep must contain 'Affliction' as a key
    :precondition: creep must contain 'Turn' as a key and a boolean value as the value
    :postcondition: determines if current_char has obtained victory in an encounter
    :return: a boolean value representing if current_char has won an encounter

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, \
                          'EXP': 100}
    >>> check_for_victory(test_char_one, test_creep_one)
    False

    >>> test_char_two = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False, \
                         'Affliction': None}
    >>> test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 0, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, \
                          'EXP': 100}
    >>> check_for_victory(test_char_two, test_creep_two)
    True
    """
    if type(current_char) is not dict or type(creep) is not dict:
        raise TypeError("Must pass dictionaries as an argument.")
    elif 'HP' not in current_char or 'HP' not in creep:
        raise KeyError("'HP' key must exist in both dictionaries.")
    else:
        return True if current_char['HP'] > 0 >= creep['HP'] else False


def encounter_victory(current_char: dict, creep: dict) -> None:
    """
    Modify a character's statistics after winning an encounter.

    :param current_char: a dictionary
    :param creep: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :precondition: creep must contain 'Name' as a key and a string as the value
    :precondition: creep must contain 'HP', 'ATK' and 'EXP' as keys with positive numbers as the value
    :precondition: creep must contain 'Affliction' as a key
    :precondition: creep must contain 'Turn' as a key and a boolean value as the value
    :postcondition: modifies the stats of current_char
    :raises: TypeError: if current_char or creep is not a dictionary
    """
    if type(current_char) is not dict or type(creep) is not dict:
        raise TypeError("Must pass dictionaries as arguments.")
    else:
        heal = random.randint(30, 50)
        mp = random.randint(30, 50)
        leveling.gain_experience(current_char=current_char, creep=creep)
        leveling.level_up(current_char=current_char)
        current_char['HP'] += heal
        current_char['MP'] += mp
        print(f"You have slain {creep['Name']}!")
        time.sleep(2)
        print(f"You have healed for {heal} HP.")
        print(f"You have regenerated {mp} mana.")
        time.sleep(2)


def spawn_boss(current_char: dict) -> dict:
    """
    Summon a boss when the player reaches the last coordinate on the floor.

    :param current_char: a dictionary
    :precondition: current_char must contain 'Name' as a key and a string as a value
    :precondition: current_char must contain 'Class' as a key and a string as a value
    :precondition: current_char must contain 'HP', 'MP', 'EXP' and 'Attack' as keys with a positive number as the value
    :precondition: current_char must contain 'X-coord', 'Y-coord', 'Z-coord' and 'Level' as keys with positive integers
                   as values
    :precondition: current_char must contain 'Turn' as a key and a boolean value as the value
    :precondition: current_char must contain 'Spell' as a key and a string as the value
    :postcondition: determines the boss spawned in an encounter
    :return: a dictionary representing a boss
    :raises: FileNotFoundError: if bosses.json does not exist in a directory named combat
    """
    with open('combat/bosses.json', 'r') as file_object:
        bosses = json.load(file_object)
    if current_char['X-coord'] == 4 and current_char['Y-coord'] == 4 and current_char['Z-coord'] == 0:
        return bosses[0]
    elif current_char['X-coord'] == 4 and current_char['Y-coord'] == 4 and current_char['Z-coord'] == 1:
        return bosses[1]
    else:
        return bosses[2]


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
