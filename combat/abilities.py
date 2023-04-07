import playsound as playsound

import combat
import time
# playsound()


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
    Cast doomsday spell on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key and a positive integer as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive integer
    :postcondition: modifies the status of creep

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
    creep['HP'] -= combat.DOOMSDAY_FLAT_DMG + (character['Attack']*combat.ATK_MULTIPLIER)
    creep['Affliction'] = 'Burn'
    print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
    # character['MP'] -= combat.DOOMSDAY_MP_COST


def stab(character, creep):
    """
    Cast stab spell on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key and a positive integer as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive integer
    :postcondition: modifies the status of creep

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
    creep['HP'] -= combat.STAB_FLAT_DMG + (character['Attack']*combat.ATK_MULTIPLIER)
    creep['Affliction'] = 'Bleed'
    print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
    # character['MP'] -= combat.STAB_MP_COST


def earthquake_chain(character, creep):
    """
    Cast earthquake_chain spell on creep

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' and 'Affliction' as a key
    :precondition: character must have 'Attack' as a key and a positive integer as the value
    :precondition: creep must have 'HP' and 'Affliction' as a key and 'HP' must be a positive integer
    :postcondition: modifies the status of creep

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
    creep['HP'] -= combat.EARTHQUAKE_CHAIN_FLAT_DMG + character['Attack']*combat.ATK_MULTIPLIER
    creep['Affliction'] = 'Stunned'
    print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
    # character['MP'] -= combat.EARTHQUAKE_CHAIN_MP_COST


def regular_attack(character, creep):
    """
    Perform an attack on creep.

    :param character: a dictionary containing 'Attack' as a key
    :param creep: a dictionary containing 'HP' as a key
    :precondition: character must be a dictionary containing 'Attack' as a key and a positive integer as the value
    :precondition: creep must be a dictionary containing 'HP' as a key and a positive integer as the value
    :postcondition: modifies the status of creep

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
    creep['HP'] -= character['Attack']
    print(f"{creep['Name']} has been hit for {character['Attack']} damage!")
    time.sleep(2)


def cast_spell(character, creep):
    skillset = {'Earthquake Chain': earthquake_chain, 'Doomsday': doomsday, 'Stab': stab}
    for key in skillset:
        if character['Spell'] == key:
            print(f"Casting {character['Spell']}...")
            skillset[key](character, creep)
            decrement_mana(character)
    # print(f"Casting {character['Spell']}...")
    # if character['Spell'] == 'Earthquake Chain':
    #     earthquake_chain(character=character, creep=creep)
    #     character['MP'] -= combat.EARTHQUAKE_CHAIN_MP_COST
    # elif character['Spell'] == 'Doomsday':
    #     doomsday(character=character, creep=creep)
    #     character['MP'] -= combat.DOOMSDAY_MP_COST
    # else:
    #     stab(character=character, creep=creep)
    #     character['MP'] -= combat.STAB_MP_COST
    # print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
    time.sleep(2)


def decrement_mana(character):
    skillset = {'Earthquake Chain': combat.EARTHQUAKE_CHAIN_MP_COST, 'Doomsday': combat.DOOMSDAY_MP_COST,
                'Stab': combat.STAB_MP_COST}
    for key in skillset:
        if character['Spell'] == key:
            character['MP'] -= skillset[key]
            print(f"You lost {character['MP']} MP.")


def main():
    """
    
    :return: 
    """


if __name__ == "__main__":
    main()
