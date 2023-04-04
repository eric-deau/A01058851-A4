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
    creep['Affliction'] = 'Dizzy'
    character['MP'] -= 30
