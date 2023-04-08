import time
from combat import DOOMSDAY_MP_COST, EARTHQUAKE_CHAIN_MP_COST, STAB_MP_COST, abilities


def character_attack(character: dict, creep: dict) -> None:
    """
    Perform an attack on a monster in an encounter.

    :param character: a dictionary
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
    :postcondition: modifies creep dictionary
    :return: None if the character runs away
    """
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    attack_choice = get_attack_choice(character)
    print(f'You decide to use: {choices[attack_choice]}')
    time.sleep(2)
    if choices[attack_choice] != 'Run away':
        determine_attack(attack_choice=choices[attack_choice], character=character, creep=creep)
        creep['Turn'] = True
        character['Turn'] = False
        print(f"Opponent health is now at: 0") if creep['HP'] <= 0 \
            else print(f"Opponent health is now at: {creep['HP']}")
        time.sleep(3)
    else:
        abilities.run_away(character)
        return


def determine_attack(attack_choice: str, character: dict, creep: dict) -> None:
    """
    Determine the choice of attack for character to perform.

    :param attack_choice: a string
    :param character: a dictionary
    :param creep: a dictionary
    :precondition: attack_choice must be a string passed from character_attack
    :precondition: character must be a dictionary passed from character_attack
    :precondition: creep must be a dictionary passed from character_attack
    :postcondition: determines the type of attack a character will perform
    :raises: TypeError: if attack_choice is not a string or character and creep is not a dictionary
    """
    if type(attack_choice) is not str:
        raise TypeError("Must pass a string as an argument.")
    elif type(character) is not dict or type(creep) is not dict:
        raise TypeError("Must pass dictionaries as arguments")
    else:
        if attack_choice == "Attack":
            abilities.regular_attack(character, creep)
        else:
            abilities.cast_spell(character, creep)


def check_for_mana(character: dict) -> bool:
    """
    Determine if the character has enough mana to perform an ability.

    :param character: a dictionary
    :precondition: character must be a dictionary passed from validate_attack_choice
    :postcondition: determines if a character has enough mana to cast an ability
    :return: a boolean value representing if a character has sufficient mana
    :raises: TypeError: if character is not a dictionary
    """
    if type(character) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    else:
        mp_costs = {'Warrior': EARTHQUAKE_CHAIN_MP_COST, 'Mage': DOOMSDAY_MP_COST, 'Thief': STAB_MP_COST}
        if character['MP'] < mp_costs[character['Class']]:
            print(f"Not enough mana for {character['Spell']}.")
            return False
        else:
            return True


def check_for_stun(creep: dict) -> bool:
    """
    Check if a creep is stunned.

    :param creep: a dictionary
    :precondition: creep must be a dictionary passed from creep_attack
    :postcondition: determines if a creep is afflicted with a stun effect
    :return: a boolean value representing if a creep is stunned
    """
    return creep['Affliction'] == 'Stunned'


def creep_attack(character: dict, creep: dict) -> None:
    """
    Perform creep action on character.

    :param character: a dictionary
    :param creep: a dictionary
    :precondition: character must be a dictionary passed from check_for_turn function in encounters module
    :precondition: creep must be a dictionary passed from check_for_turn function in encounters module
    :postcondition: inflicts an attack on character if creep is not stunned
    :raises: TypeError: if character or creep is not a dictionary
    """
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Must pass dictionaries as an argument.")
    else:
        if not check_for_stun(creep):
            print(f"{creep['Name']} is about to attack!")
            time.sleep(2)
            character['HP'] -= creep['ATK']
            creep['Turn'] = False
            character['Turn'] = True
            print(f"Your health is now at: {character['HP']}")
            time.sleep(2)
        else:
            character['Turn'] = True
            print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They can't move!")


def get_attack_choice(character: dict) -> str:
    """
    Determine the attack choice of the player.

    :param character: a dictionary
    :precondition: must be a dictionary passed from character_attack function
    :postcondition: determines the player's choice of attack
    :return: a string representing a player's choice of attack
    """
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    user_choice = get_user_choice()
    valid_move = validate_attack_choice(user_choice, choices, character)
    if valid_move:
        return user_choice
    else:
        while not valid_move:
            user_choice = get_user_choice()
            valid_move = validate_attack_choice(user_choice, choices, character)
        return user_choice


def get_user_choice() -> str:
    """
    Get the input of a user.

    :postcondition: displays the list of choices for a user and gets their input
    :return: a string representing the input of a user
    """
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    for value, name in enumerate(choices.values(), 1):
        print(f'{value}. {name}')
    return input("Select one of the choices by typing in the corresponding number: ")


def validate_attack_choice(attack_choice: str, choices: dict, character: dict) -> bool:
    """
    Determine if the attack choice of the user is valid.

    :param attack_choice: a string
    :param choices: a dictionary
    :param character: a dictionary
    :precondition: attack_choice must be a string passed from get_attack_choice function
    :precondition: choices must be a dictionary passed from get_attack_choice function
    :precondition: character must be a dictionary passed from get_attack_choice function
    :postcondition: determines if the attack choice of the user is a valid move
    :return: a boolean value representing if an attack choice is valid or not
    """
    if type(attack_choice) is not str:
        raise TypeError("Must pass a choice argument as a string.")
    elif type(choices) is not dict or type(character) is not dict:
        raise TypeError("Must pass choices and character as a dictionary.")
    else:
        if attack_choice not in choices:
            print(f"That is not a choice.")
            return False
        if attack_choice == '2':
            sufficient_mana = check_for_mana(character)
            return True if sufficient_mana else False
        return True


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
