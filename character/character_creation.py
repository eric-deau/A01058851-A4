def make_character() -> dict:
    """
    Initialize a starting character.

    :postcondition: creates a dictionary containing a character's X and Y coordinates, and the health points
    :return: a dictionary that represents a character and their attributes

    >>> test_character_one = make_character()
    >>> test_character_one
    {'X-coordinates': 0, 'Y-coordinates': 0, 'HP': 2}
    """
    create_char = {'Name': choose_name(), 'Class': choose_class(), 'Attack': None, 'Spell': None, 'MP Cost': None,
                   "X-coord": 0, "Y-coord": 0, 'Z-coord': 0, "HP": 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    determine_stats(create_char)
    create_char['Spell'] = get_skill(create_char['Class'])
    return create_char


def choose_name():
    name_count = 0
    name = input("Enter a name: ")
    confirm_name = input("Are you sure? Enter \'Y\' to confirm: ")
    while confirm_name.lower() != 'y':
        if name_count < 3:
            name = input("Okay, let's try this again. Enter a name: ")
        elif 3 < name_count < 10:
            name = input("Do you need suggestions on a name? Enter a name: ")
        else:
            name = "Amanda Hugginkiss"
            print(f"Okay, that is enough. Your name is now: {name}")
            break
        confirm_name = input("Are you sure? Enter \'Y\' to confirm: ")
        name_count += 1
    return name


def choose_class():
    classes = {'1': 'Warrior', '2': 'Mage', '3': 'Thief'}
    for value, name in enumerate(classes.values(), 1):
        print(f'{value}. {name}')
    char_class = input("Choose a class by selecting the number: ")
    char_class = valid_selection(char_class, classes)
    print(f"You have selected: {char_class}")
    confirm_class = input("Are you sure? Enter \'Y\' to confirm: ")
    while confirm_class.lower() != 'y':
        char_class = input("Choose a class by selecting the number: ")
        char_class = valid_selection(char_class, classes)
        confirm_class = input("Are you sure? Enter \'Y\' to confirm: ")
    return char_class


def get_skill(char_class):
    if char_class == 'Warrior':
        return 'Earthquake Chain'
    elif char_class == 'Mage':
        return 'Doomsday'
    else:
        return 'Sucker Punch'


def determine_stats(character):
    if character['Class'] == 'Warrior':
        warrior_stats(character)
    elif character['Class'] == 'Mage':
        mage_stats(character)
    else:
        thief_stats(character)


def warrior_stats(character):
    character['Attack'] = 50
    character['HP'] = 110
    character['MP'] = 50
    character['MP Cost']


def thief_stats(character):
    character['Attack'] = 40
    character['HP'] = 90
    character['MP'] = 100


def mage_stats(character):
    character['Attack'] = 30
    character['HP'] = 80
    character['MP'] = 150


def valid_selection(selection, classes):
    user_input = selection
    while user_input not in classes:
        print("\"Is that even a class? Let's try again.\"")
        user_input = input("Type in a number from 1-3 to pick a class: ")
    return classes[user_input]


def main():
    """
    Drive the program
    """


if __name__ == "__main__":
    main()
