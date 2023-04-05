from combat import encounters
import movement
from board import world_creation, ROWS, COLUMNS, FLOORS
from movement import movement
from utilities import game_checks


def game():
    world = world_creation.make_board(ROWS, COLUMNS, FLOORS)
    # character = character_creation.make_character()
    # print(character)
    character = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None, 'X-coord': 3,
                 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1, 'Turn': False, 'Affliction': None}
    test_boss = {'Name': 'EYE OF CTHULHU', 'Level': 2, 'HP': 1, 'ATK': 50, 'Affliction': None, 'Turn': False, 'EXP': 50}
    achieved_goal = False
    while character['HP'] > 0 and not achieved_goal:
        movement.check_for_floor_change(character)
        game_checks.reset_affliction(character)
        movement.describe_current_location(world, character)
        print("coordinates", character['X-coord'], character['Y-coord'])
        direction = movement.get_user_choice()
        valid_move = movement.validate_move(world, character, direction)
        if valid_move:
            movement.move_character(character, direction)
            # print(character['X-coord'], character['Y-coord'])
            boss_check = game_checks.check_for_boss(character, world)
            # print(boss_check)
            if boss_check:
                boss = encounters.spawn_boss(character)
                print(f"YOU HAVE ENCOUNTERED {boss['Name']}.")
                # encounters.engage_combat(character, encounters.spawn_boss(character))
                encounters.engage_combat(character, test_boss)
                world_creation.edit_floor_descriptions(character=character, board=world)
            elif game_checks.check_for_random_foes():
                encounters.decide_encounter(character)
            else:
                pass
            achieved_goal = game_checks.check_if_goal_attained(character)
        else:
            print("\"That door seems to be locked\"")
    if achieved_goal:
        game_checks.victory()
    if character['HP'] <= 0:
        print("YOU DIED.")


def main():
    game()


if __name__ == "__main__":
    main()
