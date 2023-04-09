import random
import time


def check_if_goal_attained(current_char: dict, rows: int, columns: int, floors: int) -> bool:
    """
    Check if a character meets the win condition of the game.

    :param current_char: a dictionary containing keys 'X-coord', 'Y-coord', 'Z-coord' and 'HP'
    :param rows: a positive integer
    :param columns: a positive integer
    :param floors: a positive integer
    :precondition: current_char must contain keys 'X-coord','Y-coord', 'Z-coord' and 'HP'
    :precondition: current_char key 'HP' value must be a positive integer more than 0
    :precondition: current_char keys 'X-coord' value must be a positive integer more than 0
    :precondition: current_char keys 'Y-coord' value must be a positive integer more than 0
    :precondition: current_char keys 'Z-coord' value must be a positive integer more than 0
    :precondition: rows must be a positive integer more than or equal to 2
    :precondition: columns must be a positive integer more than or equal to 2
    :precondition: floors must be a positive integer more than or equal to 1
    :postcondition: determines if current_character meets the win condition of the game
    :return: a boolean value representing the win condition of the character

    >>> test_char_one = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, 'HP': 2}
    >>> check_if_goal_attained(test_char_one)
    False

    >>> test_char_two = {'X-coord': 4, 'Y-coord': 4, 'Z-coord': 2, 'HP': 2}
    >>> check_if_goal_attained(test_char_two)
    True
    """
    if current_char["X-coord"] == rows-1 and current_char["Y-coord"] == columns-1 and \
            current_char['Z-coord'] == floors-1 and current_char['HP'] > 0:
        return True
    return False


def check_for_random_foes() -> int:
    """
    Determine if a character will have an encounter in the playing board 25% of the time.

    :postcondition: determines if a mini-game will be initialized 25% of the time
    :return: a boolean value representing if a foe is encountered 25% of the time
    """
    return random.randint(1, 4) == 1


def check_for_boss(current_char: dict, current_board: dict) -> bool:
    """
    Determine if a character will have an encounter with a boss on the playing board.

    :param current_char: a dictionary containing keys 'X-coord', 'Y-coord', 'Z-coord' and 'HP'
    :param current_board: a dictionary containing tuples of length 3 with positive integers as keys
    :precondition: current_char must contain keys 'X-coord','Y-coord', 'Z-coord' and 'HP'
    :precondition: current_char key 'HP' value must be a positive integer more than 0
    :precondition: current_char keys 'X-coord' value must be a positive integer more than 0
    :precondition: current_char keys 'Y-coord' value must be a positive integer more than 0
    :precondition: current_char keys 'Z-coord' value must be a positive integer more than 0
    :precondition: current_board tuple keys must contain three positive integers more than or equal to 0


    >>> char_one = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, 'HP': 2}
    >>> board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Test', (0, 0, 2): 'Test',\
      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test', \
      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test', \
      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test', \
      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test', \
      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test', \
      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test', \
      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test', \
      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test', \
      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test', \
      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test', \
      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test', \
      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test', \
      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test', \
      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test', (4, 4, 0): 'BOSS HERE', \
      (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
    >>> check_for_boss(char_one, board_one)
    False

    >>> char_two = {'X-coord': 4, 'Y-coord': 4, 'Z-coord': 0, 'HP': 2}
    >>> board_two = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Test', (0, 0, 2): 'Test',\
      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test', \
      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test', \
      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test', \
      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test', \
      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test', \
      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test', \
      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test', \
      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test', \
      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test', \
      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test', \
      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test', \
      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test', \
      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test', \
      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test', (4, 4, 0): 'BOSS HERE', \
      (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
    >>> check_for_boss(char_two, board_two)
    True

    >>> char_three = {'X-coord': 4, 'Y-coord': 4, 'Z-coord': 1, 'HP': 2}
    >>> board_three = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Test', (0, 0, 2): 'Test',\
      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test', \
      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test', \
      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test', \
      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test', \
      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test', \
      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test', \
      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test', \
      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test', \
      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test', \
      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test', \
      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test', \
      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test', \
      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test', \
      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test', (4, 4, 0): 'BOSS HERE', \
      (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
    >>> check_for_boss(char_three, board_three)
    True
    """
    if current_board[(current_char['X-coord'], current_char['Y-coord'], current_char['Z-coord'])] == "BOSS HERE":
        return True
    else:
        return False


def reset_affliction(current_char: dict) -> None:
    """
    Reset the affliction on current_char after an encounter is over.

    :param current_char: a dictionary containing 'Affliction' as a key
    :precondition: current_char must be a dictionary containing a key named 'Affliction'
    :postcondition: modifies current_char key 'Affliction' value to be None
    :raises: TypeError: if current_char is not a dictionary
    :raises: KeyError: if 'Affliction' is not a key existing in current_char

    >>> char_one = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, 'Affliction': 'Run Away', 'HP': 2}
    >>> reset_affliction(char_one)
    >>> char_one
    {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, 'Affliction': None, 'HP': 2}
    """
    if type(current_char) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    elif 'Affliction' not in current_char:
        raise KeyError("'Affliction' must exist in dictionary as a key.")
    else:
        if current_char['Affliction']:
            current_char['Affliction'] = None


def victory():
    pass


def defeat(input_file):
    """
    Display ascii art that indicates to users that they have lost.

    :param input_file: a string representing the name of a file
    :precondition: input_file must be a plain text file
    :precondition: input_file must be an existing file
    :postcondition: displays an ascii art that tells users they died
    :raises: FileNotFoundError: if input_file does not exist in the directory
    """
    with open(input_file, 'r') as file_object:
        content = file_object.readlines()
    for line in content:
        print(f'{line}', end="")
        time.sleep(0.25)
    print()


def main():
    """
    Drive the program.
    """
    defeat('defeat_ascii.txt')


if __name__ == "__main__":
    main()
