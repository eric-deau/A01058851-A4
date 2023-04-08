import combat
import time


def run_away(character):
    """
    Perform the run away ability on character.

    :param character: a dictionary
    :precondition: character must contain a key called 'Affliction'
    :postcondition: modifies character 'Affliction' status

    >>> test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None, \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> run_away(test_char)
    >>> test_char['Affliction']
    'Coward'
    >>> test_char['X-coord']
    0
    >>> test_char['Y-coord']
    0
    """
    if type(character) is not dict:
        raise TypeError("Argument must be a dictionary.")
    elif 'Affliction' not in character or 'X-coord' not in character or 'Y-coord' not in character:
        raise KeyError("'Affliction', 'X-coord' and 'Y-coord' keys must be in the dictionary.")
    elif character['X-coord'] < 0 or character['Y-coord'] < 0:
        raise ValueError("'X-coord' and 'Y-coord' keys must be a positive integer.")
    else:
        character['Affliction'] = 'Coward'
        character['X-coord'] = 0
        character['Y-coord'] = 0


def doomsday(character, creep):
    """
    Cast doomsday ability on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key with a positive number as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive number
    :postcondition: modifies the status of creep
    :raises: TypeError: if character and creep are not dictionaries
    :raises: KeyError: if 'Affliction and 'HP' are not in creep dictionary or 'Attack' not in character dictionary
    :raises: ValueError: if character 'Attack' key or creep 'HP' key is not a positive number
    >>> test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> doomsday(test_char, test_creep)
    >>> test_creep['HP']
    -26.0
    >>> test_creep['Affliction']
    'Burn'
    """
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'Affliction' not in creep or 'HP' not in creep or 'Attack' not in character:
        raise KeyError("'Affliction' and 'HP' keys must be in creep dictionary"
                       "and 'Attack' key must be in character dictionary.")
    elif character['Attack'] < 0 or creep['HP'] < 0:
        raise ValueError("Character's 'Attack' and Creep's 'HP' keys must be a positive integer.")
    else:
        creep['HP'] -= combat.DOOMSDAY_FLAT_DMG + (character['Attack']*combat.ATK_MULTIPLIER)
        creep['Affliction'] = 'Burn'
        print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
        # character['MP'] -= combat.DOOMSDAY_MP_COST


def stab(character, creep):
    """
    Cast stab ability on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key with a positive number as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive number
    :postcondition: modifies the status of creep
    :raises: TypeError: if character and creep are not dictionaries
    :raises: KeyError: if 'Affliction and 'HP' are not in creep dictionary or 'Attack' not in character dictionary
    :raises: ValueError: if character 'Attack' key or creep 'HP' key is not a positive number

    >>> test_char = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 30, 'Spell': 'Stab', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> stab(test_char, test_creep)
    >>> test_creep['HP']
    -6.0
    >>> test_creep['Affliction']
    'Bleed'
    """
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'Affliction' not in creep or 'HP' not in creep or 'Attack' not in character:
        raise KeyError("'Affliction' and 'HP' keys must be in creep dictionary"
                       "and 'Attack' key must be in character dictionary.")
    elif character['Attack'] < 0 or creep['HP'] < 0:
        raise ValueError("Character's 'Attack' and Creep's 'HP' keys must be a positive integer.")
    else:
        creep['HP'] -= combat.STAB_FLAT_DMG + (character['Attack']*combat.ATK_MULTIPLIER)
        creep['Affliction'] = 'Bleed'
        print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
        # character['MP'] -= combat.STAB_MP_COST


def earthquake_chain(character, creep):
    """
    Cast earthquake_chain ability on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key with a positive number as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive number
    :postcondition: modifies the status of creep
    :raises: TypeError: if character and creep are not dictionaries
    :raises: KeyError: if 'Affliction and 'HP' are not in creep dictionary or 'Attack' not in character dictionary
    :raises: ValueError: if character 'Attack' key or creep 'HP' key is not a positive number

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> earthquake_chain(test_char_one, test_creep_one)
    EYE OF CTHULHU has been afflicted with Stunned!
    >>> test_creep_one['HP']
    -16.0
    >>> test_creep_one['Affliction']
    'Stunned'

    >>> test_char_two = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 100, 'Spell': 'Earthquake Chain', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 2, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 150, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> earthquake_chain(test_char_two, test_creep_two)
    EYE OF CTHULHU has been afflicted with Stunned!
    >>> test_creep_two['HP']
    100.0
    >>> test_creep_two['Affliction']
    'Stunned'
    """
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'Affliction' not in creep or 'HP' not in creep or 'Attack' not in character:
        raise KeyError("'Affliction' and 'HP' keys must be in creep dictionary"
                       "and 'Attack' key must be in character dictionary.")
    elif character['Attack'] < 0 or creep['HP'] < 0:
        raise ValueError("Character's 'Attack' and Creep's 'HP' keys must be a positive integer.")
    else:
        creep['HP'] -= combat.EARTHQUAKE_CHAIN_FLAT_DMG + character['Attack']*combat.ATK_MULTIPLIER
        creep['Affliction'] = 'Stunned'
        print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
        # character['MP'] -= combat.EARTHQUAKE_CHAIN_MP_COST


def regular_attack(character, creep):
    """
    Perform an attack on creep.

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' as a key
    :precondition: character must be a dictionary containing 'Attack' as a key with a positive number as the value
    :precondition: creep must be a dictionary containing 'HP' as a key with a positive number as the value
    :postcondition: modifies the status of creep
    :raises: TypeError: if character and creep are not dictionaries
    :raises: KeyError: if 'HP' is not in creep dictionary as a key or 'Attack' not in character dictionary as a key
    :raises: ValueError: if character 'Attack' key or creep 'HP' key is not a positive number

    >>> test_char_one = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> regular_attack(test_char_one, test_creep_one)
    EYE OF CTHULHU has been hit for 80 damage!
    >>> test_creep_one['HP']
    -50

    >>> test_char_two = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 40, 'Spell': 'Earthquake Chain', \
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1, \
                     'Turn': False, 'Affliction': None}
    >>> test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 80, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> regular_attack(test_char_two, test_creep_two)
    EYE OF CTHULHU has been hit for 40 damage!
    >>> test_creep_two['HP']
    40
    """
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'HP' not in creep or 'Attack' not in character:
        raise KeyError("'HP' keys must be in creep dictionary and 'Attack' key must be in character dictionary.")
    elif character['Attack'] < 0 or creep['HP'] < 0:
        raise ValueError("Character's 'Attack' and Creep's 'HP' keys must be a positive integer.")
    else:
        creep['HP'] -= character['Attack']
        print(f"{creep['Name']} has been hit for {character['Attack']} damage!")
        time.sleep(2)


def cast_spell(character, creep):
    """
    Cast an ability depending on what the character's spell is.

    :param character: a dictionary with 'MP' as a key with a positive number as the value, and 'Spell' as a key with
                      a string as the value
    :param creep: a dictionary with 'HP' as a key with a positive number as the value
    :precondition: character must be a dictionary containing 'MP' as a key with a positive number as the value
    :precondition: character must be a dictionary containing 'Spell' as a key with 'Earthquake Chain', 'Doomsday',
                   or 'Stab' as the value
    :precondition: creep must be a dictionary containing 'HP' as a key with a positive number as the value
    :raises: TypeError: if character and creep are not dictionaries
    :raises: KeyError: if 'HP' is not in creep dictionary as a key or 'Spell' not in character dictionary as a key
    :raises: ValueError: if character 'Spell' key is not 'Earthquake Chain', 'Stab', or 'Doomsday'
                         and creep 'HP' key is not a positive number
    """
    skillset = {'Earthquake Chain': earthquake_chain, 'Doomsday': doomsday, 'Stab': stab}
    if type(character) is not dict or type(creep) is not dict:
        raise TypeError("Arguments must be a dictionary.")
    elif 'HP' not in creep or 'Spell' not in character:
        raise KeyError("'HP' keys must be in creep dictionary and 'Attack' key must be in character dictionary.")
    elif character['Spell'] not in skillset or creep['HP'] < 0:
        raise ValueError("Character must contain a spell called 'Earthquake Chain', 'Stab', or 'Doomsday',"
                         " and Creep's 'HP' keys must be a positive integer.")
    else:
        print(f"Casting {character['Spell']}...")
        skillset[character['Spell']](character=character, creep=creep)
        decrement_mana(character)
        time.sleep(2)


def decrement_mana(character):
    """
    Decrease the mana of a character based on the skill used.

    :param character: a dictionary with 'MP' as a key with a positive number as the value, and 'Spell' as a key with
                      a string as the value
    :precondition: character must be a dictionary with 'MP' and 'Spell' as a key
    :precondition: character 'MP' key must have a positive number as a value
    :precondition: character 'Spell' key must contain 'Earthquake Chain', 'Stab', or 'Doomsday' as a value
    :postcondition: modifies character 'MP' key
    :raises: TypeError: if character is not a dictionary
    :raises: KeyError: if 'MP' or 'Spell' do not exist in character dictionary
    :raises: ValueError: if character 'MP' key is less than zero or character 'Spell' key does not have a value of
                         'Earthquake Chain', 'Stab' or 'Doomsday'
    """
    skillset = {'Earthquake Chain': combat.EARTHQUAKE_CHAIN_MP_COST, 'Doomsday': combat.DOOMSDAY_MP_COST,
                'Stab': combat.STAB_MP_COST}
    if type(character) is not dict:
        raise TypeError("Argument must be a dictionary.")
    elif 'MP' not in character or 'Spell' not in character:
        raise KeyError("'HP' and 'Spell' must be in character as a key.")
    elif character['Spell'] not in skillset or character['MP'] < skillset[character['Spell']]:
        raise ValueError("Character must contain a spell called 'Earthquake Chain', 'Stab', or 'Doomsday' and character"
                         "'MP' must be more than 0.")
    else:
        character['MP'] -= skillset[character['Spell']]
        print(f"You lost {skillset[character['Spell']]} MP.")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
