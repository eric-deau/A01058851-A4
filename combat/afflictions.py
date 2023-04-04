from combat import BURNING_DMG, BLEED_DMG


def check_for_creep_afflictions(creep, character):
    if creep['Affliction'] == 'Burn':
        burning(creep)
    if creep['Affliction'] == 'Stunned':
        stun(creep, character=character)
    if creep['Affliction'] == 'Bleeding':
        bleed(creep=creep)


def burning(creep):
    creep['HP'] -= 2
    print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They have taken {BURNING_DMG} damage.")


def bleed(creep):
    creep['HP'] -= 7
    print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They have taken {BLEED_DMG} damage.")


def stun(creep, character):
    creep['Turn'] = False
    character['Turn'] = True
    print(f"{creep['Name']} is afflicted with {creep['Affliction']}! They can't move!")


def main():
    """

    :return:
    """


if __name__ == "__main__":
    main()
