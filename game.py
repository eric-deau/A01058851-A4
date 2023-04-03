import character_creation
import movement
import encounters


def game():

    character = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
    while character['HP'] > 0:
        creep = encounters.spawn_monster()
        while character['HP'] > 0 and creep['HP'] > 0:
            encounters.engage_combat(character, creep)


def main():
    game()


if __name__ == "__main__":
    main()
