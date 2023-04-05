from character import LEVEL_TWO, LEVEL_THREE


def gain_experience(character, creep):
    character['EXP'] += creep['EXP']
    if LEVEL_THREE > character['EXP'] > LEVEL_TWO and character['Level'] == 1:
        level_up(character)
    elif character['EXP'] > LEVEL_THREE and character['EXP'] == 2:
        level_up(character)
    else:
        print(f"{creep['EXP']} experience points gained.")


def level_up(character):
    character['Level'] += 1
    character['Attack'] += 20
    character['HP'] = 150
    character['MP'] = 150
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
