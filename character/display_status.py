def display_status(character):
    """
    Display the characteristics of a character.

    :param character: a dictionary
    :precondition: character must be a dictionary containing 'Name', 'Class', 'HP', 'MP', 'Level', 'EXP' and
                    'Affliction'
    :postcondition: prints the relevant characteristics of a character

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, \
                        'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    >>> display_status(test_char_one)
    Here is your status for RAKSHASA
    Name: RAKSHASA
    Class: Mage
    HP: 100
    MP: 100
    EXP: 0
    Level: 1
    """
    attributes = ('Name', 'Class', 'HP', 'MP', 'EXP', 'Level', 'Affliction')
    print(f"Here is your status for {character['Name']}")
    for key, value in character.items():
        if key in attributes:
            print(f"{key}: {value}")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
