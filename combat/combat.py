import time
from combat import abilities
from combat import DOOMSDAY_MP_COST, EARTHQUAKE_CHAIN_MP_COST, STAB_MP_COST


def character_attack(character, creep):
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    attack_choice = get_attack_choice(character)
    print(f'You decide to use: {choices[attack_choice]}')
    time.sleep(2)
    if choices[attack_choice] != 'Run away':
        determine_attack(attack_choice=choices[attack_choice], character=character, creep=creep)
        creep['Turn'] = True
        character['Turn'] = False
        print(f"Opponent health is now at: {creep['HP']}")
        time.sleep(3)
    else:
        run_away(character)
        # modify_health_combat(character, creep, choices[attack_choice])


def determine_attack(attack_choice, character, creep):
    print('determine attack', attack_choice)
    if attack_choice == "Attack":
        abilities.regular_attack(character, creep)
    else:
        abilities.cast_spell(character, creep)

    # if check_for_mana(character):
    #     if attack_choice == "Attack":
    #         abilities.regular_attack(character, creep)
    #     else:
    #         abilities.cast_spell(character, creep)
    # else:
    #     print(f"Not enough mana to cast {character['Spell']}.")


def check_for_mana(character):
    if character['MP'] < EARTHQUAKE_CHAIN_MP_COST and character['Class'] == "Warrior":
        return False
    elif character['MP'] < STAB_MP_COST and character['Class'] == "Thief":
        return False
    elif character['MP'] < DOOMSDAY_MP_COST and character['Class'] == "Mage":
        return False
    else:
        return True
    # if character['MP'] >= DOOMSDAY_MP_COST or character['MP'] >= STAB_MP_COST or \
    #         character['MP'] >= EARTHQUAKE_CHAIN_MP_COST:
    #     if character['Spell'] == "Doomsday":
    #         abilities.doomsday(character, creep)
    #     elif character['Spell'] == "Stab":
    #         abilities.stab(character, creep)
    #     else:
    #         abilities.earthquake_chain(character, creep)
    # else:
    #     print(f"Character does not have enough mana to cast {character['Spell']}.")
    #     return False


def creep_attack(character, creep):
    print(f"{creep['Name']} is about to attack!")
    time.sleep(2)
    character['HP'] -= creep['ATK']
    creep['Turn'] = False
    character['Turn'] = True
    print(f"Your health is now at: {character['HP']}")
    time.sleep(2)


def get_attack_choice(character):
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    for value, name in enumerate(choices.values(), 1):
        print(f'{value}. {name}')
    user_choice = input("Select one of the choices by typing in the corresponding number: ")
    valid_move = validate_attack_choice(user_choice, choices, character)
    if valid_move:
        return user_choice
    else:
        while not valid_move:
            for value, name in enumerate(choices.values(), 1):
                print(f'{value}. {name}')
            user_choice = input("Select one of the choices by typing in the corresponding number: ")
            valid_move = validate_attack_choice(user_choice, choices, character)
        return user_choice

    # while user_choice not in choices:
    #     user_choice = input("Hey bozo, you will die if you don't select a choice. Do it now: ")
    # if user_choice == '2':
    #     while check_for_mana(character)


def validate_attack_choice(attack_choice, choices, character):
    if attack_choice not in choices:
        print(f"That is not a choice.")
        return False
    if attack_choice == '2':
        sufficient_mana = check_for_mana(character)
        if sufficient_mana:
            return True
        else:
            print(f"Not enough mana for {character['Spell']}.")
            return False
    return True


# def modify_health_combat(character, creep, choice_of_attack):
#     if choice_of_attack == 'Attack':
#         creep['HP'] -= character[choice_of_attack]
#     elif choice_of_attack == 'Spell':
#         creep['HP'] -= 30
#         creep['Affliction'] = character['Spell']


def main():
    char = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
            'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    monster = {'Name': 'Slime', 'HP': 50, 'ATK': 10, 'Affliction': None, 'EXP': 5}
    # character_attack(char, monster)
    creep_attack(char, monster)


if __name__ == "__main__":
    main()
