import encounters
import movement
from board import world_creation
from movement import movement
from character import character_creation
from utilities import game_checks


def game():
    world = world_creation.make_board(5, 5, 3)
    print(world)
    # character = character_creation.make_character()
    # print(character)
    character = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None, 'X-coord': 0,
                 'Y-coord': 0, 'Z-coord': 0, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, 'Turn': False}
    achieved_goal = False
    while character['HP'] > 0 and not achieved_goal:
        movement.describe_current_location(world, character)
        direction = movement.get_user_choice()
        print(type(direction))
        valid_move = movement.validate_move(world, character, direction)
        if valid_move:
            movement.move_character(character, direction)
            print(character['X-coord'], character['Y-coord'])
            # boss_check = game_checks.check_for_boss(character)
            # print(boss_check)
            # if boss_check:
            #     boss = encounters.spawn_boss(character)
            #     print(f"You have encountered {boss['Name']}.")
            #     encounters.engage_combat(character, encounters.spawn_boss(character))

            if game_checks.check_for_random_foes():
                encounters.decide_encounter(character)

        # creep = encounters.spawn_monster()
        # while character['HP'] > 0 and creep['HP'] > 0:
        #     encounters.engage_combat(character, creep)
    if character['HP'] <= 0:
        print("YOU DIED.")


def main():
    game()


if __name__ == "__main__":
    main()
