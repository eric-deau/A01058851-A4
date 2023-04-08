def make_character() -> dict:
    """
    Initialize a starting character.

    :postcondition: creates a dictionary containing a character's X and Y coordinates, and the health points
    :return: a dictionary that represents a character and their attributes
    """
    create_char = {'Name': choose_name(), 'Class': choose_class(), 'Attack': None, 'Spell': None, 'MP Cost': None,
                   "X-coord": 0, "Y-coord": 0, 'Z-coord': 0, "HP": 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False,
                   'Affliction': None}
    determine_stats(create_char)
    create_char['Spell'] = get_skill(create_char['Class'])
    return create_char


def choose_name():
    """
    Determine a character's name.

    :postcondition: determines a character's name
    :return: a string presenting the name of a character
    """
    name_count = 0
    name = input("Enter a name: ")
    confirm_name = input("Are you sure? Enter \'Y\' to confirm: ")
    while confirm_name.lower() != 'y':
        if name_count < 3:
            name = input("Okay, let's try this again. Enter a name: ")
        elif 3 < name_count < 10:
            name = input("Do you need suggestions on a name? Enter a name: ")
        else:
            name = "Indecisive Player727"
            print(f"Okay, that is enough. Your name is now: {name}")
            break
        confirm_name = input("Are you sure? Enter \'Y\' to confirm: ")
        name_count += 1
    return name


def choose_class():
    """
    Determine the class of a character

    :postcondition: determines the class of a character
    :return: a string representing the class of a character
    """
    classes = {'1': 'Warrior', '2': 'Mage', '3': 'Thief'}
    for value, name in enumerate(classes.values(), 1):
        print(f'{value}. {name}')
    char_class = input("Choose a class by selecting the number: ")
    char_class = valid_selection(char_class, classes)
    print(f"You have selected: {char_class}")
    confirm_class = input("Are you sure? Enter \'Y\' to confirm: ")
    while confirm_class.lower() != 'y':
        char_class = input("Choose a class by selecting the number: ")
        char_class = valid_selection(selection=char_class, classes=classes)
        confirm_class = input("Are you sure? Enter \'Y\' to confirm: ")
    return char_class


def get_skill(char_class):
    """
    Determine the ability of one of the three classes.

    :param char_class: a string
    :precondition: must be a string representing the class of a character
    :postcondition: determines the ability of a character
    :return: a string representing the ability of a character
    :raises: TypeError: if char_class is not a string
    :raises: ValueError: if char_class does not represent a selectable character class

    >>> get_skill('Warrior')
    'Earthquake Chain'

    >>> get_skill('Mage')
    'Doomsday'
    """
    if type(char_class) != str:
        raise TypeError("Must pass a string as an argument.")
    elif char_class != 'Mage' and char_class != 'Warrior' and char_class != 'Thief':
        raise ValueError("Must pass a valid character class as an argument.")
    else:
        if char_class == 'Warrior':
            return 'Earthquake Chain'
        elif char_class == 'Mage':
            return 'Doomsday'
        else:
            return 'Stab'


def determine_stats(character):
    """
    Determine a character's stats based off of a selected character class.

    :param character: a dictionary containing 'HP', 'MP', and 'Attack' keys
    :precondition: character must be a dictionary containing 'HP', 'MP', and 'Attack' keys
    :postcondition: determines the character's stats based off of the selected character class

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': None, 'Spell': 'Doomsday', 'MP Cost': None, \
                        'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, \
                        'Turn': False, 'Affliction': None}
    >>> determine_stats(test_char_one)
    >>> test_char_one['Attack']
    30
    >>> test_char_one['HP']
    80
    >>> test_char_one['MP']
    150

    >>> test_char_two = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': None, 'Spell': 'Earthquake Chain',\
                        'MP Cost': None, 'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 100, 'MP': 100, 'EXP': 0, \
                         'Level': 1, 'Turn': False, 'Affliction': None}
    >>> determine_stats(test_char_two)
    >>> test_char_two['Attack']
    50
    >>> test_char_two['HP']
    110
    >>> test_char_two['MP']
    50
    """
    print(character['Class'])
    if type(character) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Class' not in character:
        raise KeyError("'Class' does not exist in dictionary.")
    elif character['Class'] != 'Warrior' and character['Class'] != 'Mage' and character['Class'] != 'Thief':
        raise ValueError("'Class' key must be paired with a value of 'Warrior', 'Mage', or 'Thief'.")
    else:
        def warrior_stats(warrior_char):
            warrior_char['Attack'] = 50
            warrior_char['HP'] = 110
            warrior_char['MP'] = 50

        def thief_stats(thief_char):
            thief_char['Attack'] = 40
            thief_char['HP'] = 90
            thief_char['MP'] = 100

        def mage_stats(mage_char):
            mage_char['Attack'] = 30
            mage_char['HP'] = 80
            mage_char['MP'] = 150

        if character['Class'] == 'Warrior':
            warrior_stats(character)
        elif character['Class'] == 'Mage':
            mage_stats(character)
        else:
            thief_stats(character)


# def warrior_stats(character):
#     character['Attack'] = 50
#     character['HP'] = 110
#     character['MP'] = 50


# def thief_stats(character):
#     character['Attack'] = 40
#     character['HP'] = 90
#     character['MP'] = 100


# def mage_stats(character):
#     character['Attack'] = 30
#     character['HP'] = 80
#     character['MP'] = 150


def valid_selection(selection, classes):
    """
    Verify user selection for a class.

    :param selection: a string
    :param classes: a dictionary
    :precondition: selection must be a string
    :precondition: classes must contain keys '1', '2' and '3'
    :postcondition: determines the user's selected class
    :return: a string representing the class selected by the user
    """
    user_input = selection
    while user_input not in classes:
        print("\"Is that even a class? Let's try again.\"")
        user_input = input("Type in a number from 1-3 to pick a class: ")
    return classes[user_input]


def main():
    """
    Drive the program
    """
    # print(make_character())
    character = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None, 'X-coord': 3,
                 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, 'Turn': False,
                 'Affliction': None}
    determine_stats(character)


if __name__ == "__main__":
    main()
