import time


def character_attack(character, creep):
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    attack_choice = get_attack_choice()
    print(f'You decide to use: {choices[attack_choice]}')
    time.sleep(2)
    if choices[attack_choice] != 'Run away':
        modify_health_combat(character, creep, choices[attack_choice])
    else:
        return
    creep['Turn'] = True
    character['Turn'] = False
    print(f"Opponent health is now at: {creep['HP']}")


def creep_attack(character, creep):
    print(f"{creep['Name']} is about to attack!")
    time.sleep(2)
    character['HP'] -= creep['ATK']
    creep['Turn'] = False
    character['Turn'] = True
    print(f"Your health is now at: {character['HP']}")


def get_attack_choice():
    choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
    for value, name in enumerate(choices.values(), 1):
        print(f'{value}. {name}')
    user_choice = input("Select one of the choices by typing in the corresponding number: ")
    while user_choice not in choices:
        user_choice = input("Hey bozo, you will die if you don't select a choice. Do it now: ")
    return user_choice


def modify_health_combat(character, creep, choice_of_attack):
    if choice_of_attack == 'Attack':
        creep['HP'] -= character[choice_of_attack]
    elif choice_of_attack == 'Spell':
        creep['HP'] -= 30
        creep['Affliction'] = character['Spell']

def victory():
    pass

def defeat():
    pass


def main():
    char = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
            'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    monster = {'Name': 'Slime', 'HP': 50, 'ATK': 10, 'Affliction': None, 'EXP': 5}
    # character_attack(char, monster)
    creep_attack(char, monster)


if __name__ == "__main__":
    main()
