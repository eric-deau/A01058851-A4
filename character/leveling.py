import character


def gain_experience(current_char, creep):
    """
    Determine the EXP gain of a character after a successful battle.

    :param current_char: a dictionary
    :param creep: a dictionary
    :precondition: current_char must be a dictionary containing 'EXP' as a key and a positive integer as a value
    :precondition: creep must be a dictionary containing 'EXP' as a key and a positive integer as a value
    :postcondition: modifies character EXP
    :raises: TypeError: if current_char or creep is not a dictionary
    :raises: KeyError: if 'EXP' is not a key in current_char or creep
    :raises: ValueError: if current_char 'EXP' or creep 'EXP' is less than 0

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, \
                        'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    >>> test_mob_one = {'Name': 'Slime', 'HP': 0, 'ATK': 10, 'Affliction': None, 'EXP': 10}
    >>> gain_experience(test_char_one, test_mob_one)
    10 experience points gained.
    """
    if type(current_char) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'EXP' not in current_char or 'EXP' not in creep:
        raise KeyError("Dictionaries must contain 'EXP' as a key.")
    elif current_char['EXP'] < 0 or creep['EXP'] < 0:
        raise ValueError("'EXP' keys must be more than or equal to 0.")
    else:
        current_char['EXP'] += creep['EXP']
        print(f"{creep['EXP']} experience points gained.")


def level_up(current_char):
    """
    Level up a character if they meet EXP requirements.

    :param current_char: a dictionary
    :precondition: current_char must be a dictionary containing 'EXP', 'Attack', 'HP', 'MP' as keys and
                   positive integers as values
    :postcondition: determines the level of a character
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if current_char does not contain 'Level' and 'EXP' as keys

    >>> char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,\
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 100, 'Level': 1, 'Turn': False}
    >>> level_up(char_one)
    You have leveled up! You are now level 2

    >>> char_two = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,\
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 220, 'Level': 2, 'Turn': False}
    >>> level_up(char_two)
    You have leveled up! You are now level 3

    >>> char_three = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, \
                      'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 150, 'Level': 2, 'Turn': False}
    >>> level_up(char_three)
    """
    if type(current_char) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Level' not in current_char or 'EXP' not in current_char:
        raise KeyError("Dictionary must contain 'Level' and 'EXP' as keys.")
    else:
        if character.LEVEL_THREE_REQ > current_char['EXP'] >= character.LEVEL_TWO_REQ and current_char['Level'] == 1:
            level_two(current_char=current_char)
        elif current_char['EXP'] >= character.LEVEL_THREE_REQ and current_char['Level'] == 2:
            level_three(current_char=current_char)
        else:
            return
        print(f"You have leveled up! You are now level {current_char['Level']}")


def level_two(current_char):
    """
    Increase current_char stats to match with level two stats.

    :param current_char: a dictionary
    :precondition: current_char must contain 'Attack', 'Level', 'HP' and 'MP' as keys with positive integers as values
    :postcondition: modifies current_char stats to match to level two stats
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if 'Attack', 'HP' or 'MP' do not exist as keys within current_char
    :raises: ValueError: if 'Level' is not 1 or 'Attack', 'HP', or 'MP' values are less than 0 in current_char

    >>> test_char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 120, 'Level': 1, 'Turn': False}
    >>> level_two(test_char_one)
    >>> test_char_one['Level']
    2
    >>> test_char_one['Attack']
    70
    >>> test_char_one['HP']
    300
    >>> test_char_one['MP']
    180
    """
    if type(current_char) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Attack' not in current_char or 'HP' not in current_char or 'MP' not in current_char or 'Level'\
            not in current_char:
        raise KeyError("'Attack', 'HP', 'MP' and 'Level' keys must exist in the dictionary.")
    elif current_char['Level'] != 1:
        raise ValueError("Dictionary 'Level' key must be 1.")
    elif current_char['Attack'] < 0 or current_char['HP'] < 0 or current_char['MP'] < 0:
        raise ValueError("'Attack', 'HP' and 'MP' values must be a positive integer.")
    else:
        current_char['Level'] += 1
        current_char['Attack'] += character.LEVEL_TWO_ATK
        current_char['HP'] += character.LEVEL_TWO_HP
        current_char['MP'] += character.LEVEL_TWO_MP


def level_three(current_char):
    """
    Increase current_char stats to match with level three stats.

    :param current_char: a dictionary
    :precondition: current_char must contain 'Attack', Level, 'HP' and 'MP' as keys with positive integers as values
    :postcondition: modifies current_char stats to match to level three stats
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if 'Attack', Level, 'HP' or 'MP' do not exist as keys within current_char
    :raises: ValueError: if 'Level' is not 2 or 'Attack', 'HP', or 'MP' values are less than 0 in current_char

    >>> test_char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0, \
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False}
    >>> level_three(test_char_one)
    >>> test_char_one['Level']
    3
    >>> test_char_one['Attack']
    110
    >>> test_char_one['HP']
    650
    >>> test_char_one['MP']
    325
    """
    if type(current_char) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Attack' not in current_char or 'HP' not in current_char or 'MP' not in current_char or 'Level'\
            not in current_char:
        raise KeyError("'Attack', 'HP', 'MP' and 'Level' keys must exist in the dictionary.")
    elif current_char['Level'] != 2:
        raise ValueError("Dictionary 'Level' key must be 1.")
    elif current_char['Attack'] < 0 or current_char['HP'] < 0 or current_char['MP'] < 0:
        raise ValueError("'Attack', 'HP' and 'MP' values must be a positive integer.")
    else:
        current_char['Level'] += 1
        current_char['Attack'] += character.LEVEL_THREE_ATK
        current_char['HP'] += character.LEVEL_THREE_HP
        current_char['MP'] += character.LEVEL_THREE_MP


def main():
    """

    :return:
    """
    # character = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
    #              'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 200, 'Level': 2, 'Turn': False}
    # level_up(character)


if __name__ == "__main__":
    main()
