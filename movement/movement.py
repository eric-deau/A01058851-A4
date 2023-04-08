import __init__


def describe_current_location(board: dict, current_char: dict) -> None:
    """
    Describe the current environment of a character.

    :param board: a dictionary containing tuples of length 3 with positive integers as keys
    :param current_char: a dictionary containing keys 'X-coord', 'Y-coord', 'Z-coord' and 'HP'
    :precondition: board must contain at least four tuple keys with two positive integer elements
    :precondition: board tuple keys must contain three positive integers
    :precondition: character must have keys 'X-coord', 'Y-coord' and 'Z-coord'
    :precondition: character keys 'X-coord' must be more than or equal to 0
    :precondition: character keys 'Y-coord' must be more than or equal to 0
    :precondition: character keys 'Z-coord' must be more than or equal to 0
    :postcondition: prints a description of the current environment of the character
    :raises: KeyError: if current_character 'X-coordinates' and 'Y-coordinates' doesn't exist in playing_board

    >>> char_one = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0,"HP": 2}
    >>> board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One', \
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four', \
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
    >>> describe_current_location(board_one, char_one)
    Looks like this is my starting point.
    You are currently in: Hell


    >>> char_two = {"X-coord": 0, "Y-coord": 0, "Z-coord": 1,"HP": 2}
    >>> board_two = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One', \
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four', \
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}

    >>> describe_current_location(board_two, char_two)
    Description One
    You are currently in: Earth
    """
    if (current_char['X-coord'], current_char['Y-coord'], current_char['Z-coord']) \
            not in board:
        raise KeyError("Coordinates do not exist within the board.")
    else:
        floors = {1: "Hell", 2: "Earth", 3: "Heaven"}
        current_location = (current_char['X-coord'], current_char['Y-coord'],
                            current_char['Z-coord'])
        print(board[current_location])
        print(f"You are currently in: {floors[current_char['Z-coord'] + 1]}")


def get_user_choice() -> str:
    """
    Determine the choice of the user.

    :postcondition: determines the direction that the user chose and print a prompt as a side effect
    :return: a string representing the user's choice of direction
    """
    choices = {"1": "North Door", "2": "South Door", "3": "West Door", "4": "East Door"}
    print("Options: \n", end="")
    for key, value in choices.items():
        print(key + ". " + value)
    user_input = input("\nType in a number from 1-4 to go in that direction:\n")
    while user_input not in choices:
        print("\"I don't think that is an option. Lets try again.\"")
        user_input = input("\nType in a number from 1-4 to go in that direction:\n")
    return choices[user_input]


def validate_move(board: dict, current_char: dict, current_dir: str) -> bool:
    """
    Check if x-y coordinates are in the bounds of the playing board.

    :param board: a dictionary containing tuples of length 3 with positive integers as keys
    :param current_char: a dictionary containing keys 'X-coord', 'Y-coord', 'Z-coord' and 'HP'
    :param current_dir: a string
    :precondition: board must contain at least four tuple keys of length three with positive integers
    :precondition: board tuple keys must contain three positive integers more than or equal to 0
    :precondition: current_char must have keys 'X-coord' and 'Y-coord'
    :precondition: current_char keys 'X-coord' must be more than or equal to 0
    :precondition: current_char keys 'Y-coord' must be more than or equal to 0
    :precondition: current_dir must be a string
    :postcondition: determines if current_character's set of coordinates is valid in board
    :return: a boolean value representing if a coordinate change is valid or not

    >>> char_one = {"X-coord": 0, "Y-coord": 0, "Z-coord": 1,"HP": 2}
    >>> board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One', \
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four', \
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
    >>> validate_move(board_one, char_one, "North Door")
    False

   >>> char_two = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0,"HP": 2}
    >>> board_two = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One', \
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four', \
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
    >>> validate_move(board_two, char_two, "South Door")
    True

    >>> char_three = {"X-coord": 0, "Y-coord": 0, "Z-coord": 1,"HP": 2}
    >>> board_three = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One', \
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four', \
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
    >>> validate_move(board_three, char_three, "East Door")
    True
    """
    choices = {"North Door": -1, "South Door": 1, "West Door": -1, "East Door": 1}
    valid_y_coordinate = current_char['Y-coord']
    valid_x_coordinate = current_char['X-coord']
    valid_z_coordinate = current_char['Z-coord']
    if current_dir == "North Door" or current_dir == "South Door":
        valid_y_coordinate += choices[current_dir]
    if current_dir == "East Door" or current_dir == "West Door":
        valid_x_coordinate += choices[current_dir]
    if (valid_x_coordinate, valid_y_coordinate, valid_z_coordinate) in board and current_dir in choices:
        return True
    return False


def move_character(current_character: dict, current_direction: str) -> None:
    """
    Modify a character's x and y coordinates.

    :param current_character: a dictionary containing keys 'X-coordinates', 'Y-coordinates', and 'HP'
    :param current_direction: a string
    :precondition: current_character must have keys 'X-coordinates' and 'Y-coordinates'
    :precondition: current_character keys 'X-coordinates' value must be a positive integer more than 0
    :precondition: current_character keys 'Y-coordinates' value must be a positive integer more than 0
    :precondition: current_direction must be "North Door", "South Door", "West Door", or "East Door"
    :postcondition: modifies character's key 'X-coordinates' or 'Y-coordinates' value


    >>> test_char_one = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 2}
    >>> test_dir_one = "South Door"
    >>> move_character(test_char_one, test_dir_one)
    >>> test_char_one
    {'X-coord': 0, 'Y-coord': 1, 'Z-coord': 0, 'HP': 2}

    >>> test_char_two = {'X-coord': 2, 'Y-coord': 1, 'Z-coord': 1, 'HP': 2}
    >>> test_dir_two = "West Door"
    >>> move_character(test_char_two, test_dir_two)
    >>> test_char_two
    {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, 'HP': 2}
    """
    choices = {"North Door": -1, "South Door": 1, "West Door": -1, "East Door": 1}
    if current_direction == "North Door" or current_direction == "South Door":
        current_character['Y-coord'] += choices[current_direction]
    if current_direction == "East Door" or current_direction == "West Door":
        current_character['X-coord'] += choices[current_direction]


def check_for_floor_change(character):
    """
    Move the character to the next floor.

    :param character: a dictionary
    :precondition: character must be a dictionary passed from game.py module
    :postcondition: modifies the coordinates of character
    :raises: TypeError: if character is not a dictionary
    """
    if type(character) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    if character['X-coord'] == __init__.ROWS-1 and character['Y-coord'] == __init__.COLUMNS-1 and \
            character['Z-coord'] < __init__.FLOORS-1:
        character['X-coord'] = 0
        character['Y-coord'] = 0
        character['Z-coord'] += 1
        # print(f"The roof is collapsing..")
        # time.sleep(2)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
