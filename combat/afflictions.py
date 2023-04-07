from combat import BURNING_DMG, BLEED_DMG


def check_for_creep_afflictions(creep):
    """
    Determine creep affliction status.

    :param creep: a dictionary containing 'HP', 'Turn' and 'Affliction' as keys
    :param character: a dictionary containing 'Turn' as a key
    :precondition: creep must be a dictionary containing 'HP', 'Turn', and 'Affliction' as keys
    :precondition: creep 'HP' must be a positive integer
    :postcondition: applies affliction status to creep if creep has an affliction
    :raises: TypeError: if creep or character is not a dictionary
    :raises: KeyError: if 'HP', 'Turn' or 'Affliction' not in creep or 'Turn' not in character
    :raises: ValueError: if creep 'HP' key is less than 0
    """
    # if type(creep) is not dict or type(character) is not dict:
    #     raise TypeError("Arguments must be a dictionary.")
    # elif 'HP' not in creep or 'Turn' not in creep or 'Affliction' not in creep:
    #     raise KeyError("'HP', 'Turn' and 'Affliction' must be an existing key in creep.")
    # elif 'Turn' not in character:
    #     raise KeyError("'Turn' must be a key in character.")
    # elif creep['HP'] < 0:
    #     raise ValueError("Creep 'HP' key must be more than 0.")
    # else:
    #     afflictions = {'Burn': burning, 'Bleed': bleed, 'Stunned': stun}
    #     if creep['Affliction'] in afflictions and creep['Affliction'] != 'Stunned':
    #         afflictions[creep['Affliction']](creep)
    #     elif creep['Affliction'] in afflictions and creep['Affliction'] == 'Stunned':
    afflictions = {'Burn': burning, 'Bleed': bleed, 'Stunned': stun}
    if creep['Affliction'] in afflictions:
        afflictions[creep['Affliction']](creep)


        # if creep['Affliction'] == 'Burn':
        #     burning(creep)
        # if creep['Affliction'] == 'Stunned':
        #     stun(creep, character=character)
        # if creep['Affliction'] == 'Bleeding':
        #     bleed(creep=creep)


def burning(creep):
    """

    :param creep:
    :return:
    """
    creep['HP'] -= BURNING_DMG
    print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They have taken {BURNING_DMG} damage.")


def bleed(creep):
    """

    :param creep:
    :return:
    """
    creep['HP'] -= BLEED_DMG
    print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They have taken {BLEED_DMG} damage.")


def stun(creep):
    """

    :param creep:
    :return:
    """
    if creep['Affliction'] == 'Stunned':
        creep['Turn'] = False
        # character['Turn'] = True
    else:
        return


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
