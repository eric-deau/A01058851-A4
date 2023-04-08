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
        # status_check = input("Would you like to see your status? Type 'Y' to check, else input anything to proceed.")
        display_status.display_status(character)
        movement.check_for_floor_change(character, __init__.ROWS, __init__.COLUMNS, __init__.FLOORS)
        game_checks.reset_affliction(character)
        movement.describe_current_location(world, character)
        direction = movement.get_user_move()
        valid_move = movement.validate_move(world, character, direction)
        if valid_move:
            movement.move_character(character, direction)
            boss_check = game_checks.check_for_boss(character, world)
            if boss_check:
                boss = encounters.spawn_boss(character)
                print(f"YOU HAVE ENCOUNTERED {boss['Name']}.")
                encounters.engage_combat(character, boss)
            elif game_checks.check_for_random_foes():
                if encounters.decide_encounter():
                    encounters.engage_combat(current_char=character, creep=encounters.spawn_monster())
                else:
                    encounters.guessing_game(current_char=character)
            else:
                pass
            achieved_goal = game_checks.check_if_goal_attained(character, rows=__init__.ROWS,
                                                               columns=__init__.COLUMNS, floors=__init__.FLOORS)
        else:
            print("\"That door seems to be locked\"")
    if character['HP'] <= 0:
        # game_checks.defeat()
        print("YOU DIED.")
    if achieved_goal:
        # game_checks.victory()
        print("Victory!")


def main():
    game()


if __name__ == "__main__":
    main()
