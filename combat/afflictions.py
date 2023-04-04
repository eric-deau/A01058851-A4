def check_for_creep_afflictions(creep, character):
    if creep['Affliction'] == 'Burn':
        burning(creep)
    if creep['Affliction'] == 'Stunned':
        stun(creep, character=character)
    if creep['Affliction'] == 'Bleeding':
        bleed(creep=creep)


def burning(creep):
    creep['HP'] -= 2


def bleed(creep):
    creep['HP'] -= 7


def stun(creep, character):
    creep['Turn'] = False
    character['Turn'] = True


def main():
    """

    :return:
    """


if __name__ == "__main__":
    main()
