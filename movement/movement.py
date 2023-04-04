def describe_current_location(current_board: dict, current_character: dict) -> None:
    """
    Describe the current environment of a character.

    :param current_board: a dictionary containing tuples of length 2 with positive integers as keys
    :param current_character: a dictionary containing keys 'X-coordinates', 'Y-coordinates', and 'HP'
    :precondition: current_board must contain at least four tuple keys with two positive integer elements
    :precondition: current_board tuple keys must contain two positive integers
    :precondition: current_character must have keys 'X-coordinates' and 'Y-coordinates'
    :precondition: current_character keys 'X-coordinates' must be more than or equal to 0
    :precondition: current_character keys 'Y-coordinates' must be more than or equal to 0
    :postcondition: prints a description of the current environment of the character
    :raises: KeyError: if current_character 'X-coordinates' and 'Y-coordinates' doesn't exist in playing_board

    >>> char_one = {"X-coordinates": 0, "Y-coordinates": 0, "HP": 2}
    >>> board_one = {(0, 0): '"A seemingly empty room. This room also has a door on each side."',\
                     (0, 1): '"A somewhat empty room. This room also has a door on each side."',\
                     (1, 0): '"A non-empty room. This room also has a door on each side."', \
                     (1, 1): '"A room. This room also has a door on each side."'}
    >>> describe_current_location(board_one, char_one)
    "A seemingly empty room. This room also has a door on each side."

    >>> char_two = {"X-coordinates": 1, "Y-coordinates": 0, "HP": 2}
    >>> board_two = {(0, 0): '"A seemingly empty room. This room also has a door on each side."',\
                     (0, 1): '"A somewhat empty room. This room also has a door on each side."',\
                     (1, 0): '"A non-empty room. This room also has a door on each side."', \
                     (1, 1): '"A room. This room also has a door on each side."'}
    >>> describe_current_location(board_two, char_two)
    "A non-empty room. This room also has a door on each side."
    """
    if (current_character['X-coord'], current_character['Y-coord'], current_character['Z-coord']) \
            not in current_board:
        raise KeyError("Coordinates do not exist within the board.")
    else:
        current_location = (current_character['X-coord'], current_character['Y-coord'],
                            current_character['Z-coord'])
        print(current_board[current_location])


# def change_floor(character, board):
#     if (character['X-coord'], character['Y-coord'], character['Z-coord']) in board:
#         character['Z-coord'] -= 1


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


def validate_move(current_board: dict, current_character: dict, current_direction: str) -> bool:
    """
    Check if x-y coordinates are in the bounds of the playing board.

    :param current_board: a dictionary containing tuples of length 2 with positive integers as keys
    :param current_character: a dictionary containing keys 'X-coordinates', 'Y-coordinates', and 'HP'
    :param current_direction: a string
    :precondition: current_board must contain at least four tuple keys of length two with positive integers
    :precondition: current_board tuple keys must contain two positive integers more than 0
    :precondition: current_character must have keys 'X-coordinates' and 'Y-coordinates'
    :precondition: current_character keys 'X-coordinates' must be more than 0
    :precondition: current_character keys 'Y-coordinates' must be more than 0
    :precondition: current_direction must be a string
    :postcondition: determines if current_character's set of coordinates is valid in the playing board
    :return: a boolean value representing if a coordinate change is valid or not

    >>> test_character_one = {"X-coordinates": 0, "Y-coordinates": 0, "HP": 2}
    >>> test_board_one = {(0,0): "Test Room", (0,1): "Test Room", (0,2): "Test Room", (1,0): "Test Room",\
     (1,1): "Test Room", (1,2) : "Test Room", (2,0): "Test Room", (2,1): "Test Room", (2,2): "Test Room"}
    >>> validate_move(test_board_one, test_character_one, "North Door")
    False

    >>> test_character_two = {"X-coordinates": 0, "Y-coordinates": 0, "HP": 2}
    >>> test_board_two = {(0,0): "Test Room", (0,1): "Test Room", (0,2): "Test Room", (1,0): "Test Room",\
     (1,1): "Test Room", (1,2) : "Test Room", (2,0): "Test Room", (2,1): "Test Room", (2,2): "Test Room"}
    >>> validate_move(test_board_two, test_character_two, "South Door")
    True

    >>> test_character_three = {"X-coordinates": 0, "Y-coordinates": 0, "HP": 2}
    >>> test_board_two = {(0,0): "Test Room", (0,1): "Test Room", (0,2): "Test Room", (1,0): "Test Room",\
     (1,1): "Test Room", (1,2) : "Test Room", (2,0): "Test Room", (2,1): "Test Room", (2,2): "Test Room"}
    >>> validate_move(test_board_two, test_character_two, "East Door")
    True
    """
    choices = {"North Door": -1, "South Door": 1, "West Door": -1, "East Door": 1}
    valid_y_coordinate = current_character['Y-coord']
    valid_x_coordinate = current_character['X-coord']
    valid_z_coordinate = current_character['Z-coord']
    if current_direction == "North Door" or current_direction == "South Door":
        valid_y_coordinate += choices[current_direction]
    if current_direction == "East Door" or current_direction == "West Door":
        valid_x_coordinate += choices[current_direction]
    if (valid_x_coordinate, valid_y_coordinate, valid_z_coordinate) in current_board and current_direction in choices:
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

    >>> test_char_one = {'X-coordinates': 0, 'Y-coordinates': 0, 'HP': 2}
    >>> test_dir_one = "South Door"
    >>> move_character(test_char_one, test_dir_one)
    >>> test_char_one
    {'X-coordinates': 0, 'Y-coordinates': 1, 'HP': 2}

    >>> test_char_two = {'X-coordinates': 2, 'Y-coordinates': 1, 'HP': 2}
    >>> test_dir_two = "West Door"
    >>> move_character(test_char_two, test_dir_two)
    >>> test_char_two
    {'X-coordinates': 1, 'Y-coordinates': 1, 'HP': 2}
    """
    choices = {"North Door": -1, "South Door": 1, "West Door": -1, "East Door": 1}
    if current_direction == "North Door" or current_direction == "South Door":
        current_character['Y-coord'] += choices[current_direction]
    if current_direction == "East Door" or current_direction == "West Door":
        current_character['X-coord'] += choices[current_direction]


def main():
    """

    :return:
    """


if __name__ == "__main__":
    main()
