import character


def gain_experience(current_char, creep):
    current_char['EXP'] += creep['EXP']
    # if character.LEVEL_THREE_REQ > current_char['EXP'] > character.LEVEL_TWO_REQ and current_char['Level'] == 1:
    #     level_up(current_char)
    # elif current_char['EXP'] > character.LEVEL_THREE_REQ and current_char['EXP'] == 2:
    #     level_up(current_char)
    # else:
    #     print(f"{creep['EXP']} experience points gained.")
    print(f"{creep['EXP']} experience points gained.")


def level_up(current_char):
    print('level up', current_char['EXP'])
    if character.LEVEL_THREE_REQ >= current_char['EXP'] >= character.LEVEL_TWO_REQ and current_char['Level'] == 1:
        current_char['Attack'] += character.LEVEL_TWO_ATK
        current_char['HP'] += character.LEVEL_TWO_HP
        current_char['MP'] += character.LEVEL_TWO_MP
    elif current_char['EXP'] >= character.LEVEL_THREE_REQ and current_char['EXP'] == 2:
        current_char['Attack'] += character.LEVEL_THREE_ATK
        current_char['HP'] += character.LEVEL_THREE_HP
        current_char['MP'] += character.LEVEL_THREE_MP
    else:
        return
    current_char['Level'] += 1
    # if current_char['Level'] == 1:
    #     current_char['Attack'] += character.LEVEL_TWO_ATK
    #     current_char['HP'] += character.LEVEL_TWO_HP
    #     current_char['MP'] += character.LEVEL_TWO_MP
    # if current_char['Level'] == 2:
    #     current_char['Attack'] += character.LEVEL_THREE_ATK
    #     current_char['HP'] += character.LEVEL_THREE_HP
    #     current_char['MP'] += character.LEVEL_THREE_MP
    print(f"You have leveled up!")


def main():
    """

    :return:
    """
    # character = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
    #              'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    # level_up(character)


if __name__ == "__main__":
    main()
