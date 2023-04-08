from combat import BURNING_DMG, BLEED_DMG


def check_for_creep_afflictions(creep):
    """
    Determine creep affliction status.

    :param creep: a dictionary containing 'HP', 'Turn' and 'Affliction' as keys
    :precondition: creep must be a dictionary containing 'HP', 'Turn', and 'Affliction' as keys
    :precondition: creep 'HP' must be a positive number
    :postcondition: applies affliction status to creep if creep has an affliction
    :raises: TypeError: if creep is not a dictionary
    :raises: KeyError: if 'HP', 'Turn' or 'Affliction' not in creep

    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, \
                      'EXP': 100}
    >>> check_for_creep_afflictions(test_creep_one)
    
    >>> test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, \
                      'EXP': 100}
    >>> check_for_creep_afflictions(test_creep_two)
    EYE OF CTHULHU is afflicted with Burn! They have taken 5 damage.
    >>> test_creep_two
    {'Name': 'EYE OF CTHULHU', 'HP': 25, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, 'EXP': 100}

    >>> test_creep_three = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': True, \
                      'EXP': 100}
    >>> check_for_creep_afflictions(test_creep_three)
    >>> test_creep_three
    {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False, 'EXP': 100}
    """
    if type(creep) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'HP' not in creep or 'Turn' not in creep or 'Affliction' not in creep:
        raise KeyError("Dictionary must contain 'HP', 'Turn' and 'Affliction' as keys.")
    else:
        afflictions = {'Burn': damage_over_time, 'Bleed': damage_over_time, 'Stunned': stun}
        if creep['Affliction'] in afflictions:
            afflictions[creep['Affliction']](creep)


def damage_over_time(creep):
    """
    Decrement the health of creep.

    :param creep: a dictionary containing 'HP'
    :precondition: creep must be a dictionary containing 'HP'
    :precondition: creep 'HP' must be a positive number
    :postcondition: decrements creep 'HP' key
    :raises: TypeError: if creep is not a dictionary
    :raises: KeyError: if 'HP' not in creep

    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, \
                          'EXP': 100}
    >>> damage_over_time(test_creep_one)
    EYE OF CTHULHU is afflicted with Burn! They have taken 5 damage.
    >>> test_creep_one
    {'Name': 'EYE OF CTHULHU', 'HP': 25, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, 'EXP': 100}

    >>> test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, \
                          'EXP': 100}
    >>> damage_over_time(test_creep_two)
    EYE OF CTHULHU is afflicted with Bleed! They have taken 15 damage.
    >>> test_creep_two
    {'Name': 'EYE OF CTHULHU', 'HP': 15, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, 'EXP': 100}
    """
    if type(creep) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'HP' not in creep:
        raise KeyError("Dictionary must contain 'HP' as a key.")
    else:
        skill_damage = {'Burn': BURNING_DMG, 'Bleed': BLEED_DMG}
        creep['HP'] -= skill_damage[creep['Affliction']]
        print(f"{creep['Name']} is afflicted with {creep['Affliction']}!"
              f" They have taken {skill_damage[creep['Affliction']]} damage.")


def stun(creep):
    """
    Apply stun effects to creep

    :param creep: a dictionary containing 'Turn'
    :precondition: creep must be a dictionary containing 'Turn'
    :postcondition: modifies creep 'Turn' key if stunned
    :raises: TypeError: if creep is not a dictionary
    :raises: KeyError: if 'HP' not in creep

    >>> test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Burn', 'Turn': True, \
                          'EXP': 100}
    >>> stun(test_creep_one)
    {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False, 'EXP': 100}
    """
    if type(creep) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Turn' not in creep:
        raise KeyError("Dictionary must contain 'Turn' as a key.")
    else:
        creep['Turn'] = False


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
