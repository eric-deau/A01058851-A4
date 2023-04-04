def doomsday(character, creep):
    creep['HP'] -= 50
    creep['Affliction'] = 'Burn'
    character['MP'] -= 50


def stab(character, creep):
    creep['HP'] -= 30
    creep['Affliction'] = 'Bleed'
    character['MP'] -= 30


def earthquake_chain(character, creep):
    creep['HP'] -= 30
    creep['Affliction'] = 'Stunned'
    character['MP'] -= 30
    print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")


def regular_attack(character, creep):
    creep['HP'] -= character['Attack']
    print(f"{creep['Name']} has been hit!")


def cast_spell(character, creep):
    print(f"Casting {character['Spell']}...")
    if character['Spell'] == 'Earthquake Chain':
        earthquake_chain(character=character, creep=creep)
    elif character['Spell'] == 'Doomsday':
        doomsday(character=character, creep=creep)
    else:
        stab(character=character, creep=creep)


def main():
    """
    
    :return: 
    """


if __name__ == "__main__":
    main()
