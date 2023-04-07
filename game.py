from combat import encounters
from board import world_creation
from movement import movement
from utilities import game_checks
from character import character_creation, display_status
import __init__


def game():
    world = world_creation.make_board(__init__.ROWS, __init__.COLUMNS, __init__.FLOORS)
    character = character_creation.make_character()
    achieved_goal = False
    while character['HP'] > 0 and not achieved_goal:
        display_status.display_status(character)
        movement.check_for_floor_change(character)
        game_checks.reset_affliction(character)
        movement.describe_current_location(world, character)
        print("coordinates", character['X-coord'], character['Y-coord'], character['Z-coord'])
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
                encounters.engage_combat(character, encounters.spawn_boss(character))
                # encounters.engage_combat(character, test_boss)
                # world_creation.edit_floor_descriptions(character=character, board=world)
            elif game_checks.check_for_random_foes():
                encounters.decide_encounter(character)
            else:
                pass
            achieved_goal = game_checks.check_if_goal_attained(character)
        else:
            print("\"That door seems to be locked\"")
    if achieved_goal:
        # game_checks.victory()
        print("Victory!")
    if character['HP'] <= 0:
        print("YOU DIED.")


def main():
    game()


if __name__ == "__main__":
    main()
