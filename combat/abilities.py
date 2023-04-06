import playsound as playsound

import combat
import time

# playsound()


def run_away(character):
    character['Affliction'] = 'Coward'
    character['X-coord'] = 0
    character['Y-coord'] = 0
    print("test", character)


def doomsday(character, creep):
    creep['HP'] -= combat.DOOMSDAY_FLAT_DMG + (character['Attack']*combat.ATK_MULTIPLIER)
    creep['Affliction'] = 'Burn'
    character['MP'] -= combat.DOOMSDAY_MP_COST


def stab(character, creep):
    creep['HP'] -= combat.STAB_FLAT_DMG * (character['Attack']*combat.ATK_MULTIPLIER)
    creep['Affliction'] = 'Bleed'
    character['MP'] -= combat.STAB_MP_COST


def earthquake_chain(character, creep):
    creep['HP'] -= combat.EARTHQUAKE_CHAIN_FLAT_DMG * (character['Attack']*combat.ATK_MULTIPLIER)
    creep['Affliction'] = 'Stunned'
    character['MP'] -= combat.EARTHQUAKE_CHAIN_MP_COST
    print(f"{creep['Name']} has been afflicted with {creep['Affliction']}!")
    time.sleep(2)


def regular_attack(character, creep):
    creep['HP'] -= character['Attack']
    print(f"{creep['Name']} has been hit!")
    time.sleep(2)


def cast_spell(character, creep):
    print(f"Casting {character['Spell']}...")
    if character['Spell'] == 'Earthquake Chain':
        earthquake_chain(character=character, creep=creep)
        character['MP'] -= 20
    elif character['Spell'] == 'Doomsday':
        doomsday(character=character, creep=creep)
        character['MP'] -= 35
    else:
        stab(character=character, creep=creep)
        character['MP'] -= 15


def main():
    """
    
    :return: 
    """


if __name__ == "__main__":
    main()
