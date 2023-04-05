from combat import DOOMSDAY_MP_COST, EARTHQUAKE_CHAIN_MP_COST, STAB_MP_COST
import time


def run_away(character):
    character['Affliction'] = 'Coward'
    character['X-coord'] = 0
    character['Y-coord'] = 0
    print("test", character)


def doomsday(character, creep):
    creep['HP'] -= 50
    creep['Affliction'] = 'Burn'
    character['MP'] -= DOOMSDAY_MP_COST


def stab(character, creep):
    creep['HP'] -= 30
    creep['Affliction'] = 'Bleed'
    character['MP'] -= STAB_MP_COST


def earthquake_chain(character, creep):
    creep['HP'] -= 30
    creep['Affliction'] = 'Stunned'
    character['MP'] -= EARTHQUAKE_CHAIN_MP_COST
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
        character['MP'] -= 10
    elif character['Spell'] == 'Doomsday':
        doomsday(character=character, creep=creep)
        character['MP'] -= 15
    else:
        stab(character=character, creep=creep)
        character['MP'] -= 10


def main():
    """
    
    :return: 
    """


if __name__ == "__main__":
    main()
