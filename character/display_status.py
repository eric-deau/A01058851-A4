def display_status(character):
    print(f"Here is your status for {character['Name']}")
    for key, value in character.items():
        print(f"{key}: {value}")


def main():
    """

    :return:
    """
    character = {'Name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    display_status(character)


if __name__ == "__main__":
    main()
