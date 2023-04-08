import random
from itertools import product


def make_board(rows: int, columns: int, floors: int) -> dict:
    """
    Initialize a playing board for a game.

    :param rows: a positive integer more than or equal to two
    :param columns: a positive integer more than or equal to two
    :param floors: a positive integer more than or equal to one
    :precondition: rows must be a positive integer more than or equal to two
    :precondition: columns must be a positive integer more than or equal to two
    :precondition: floors must be a positive integer more than or equal to two
    :postcondition: creates a dictionary representing a playing board
    :return: a dictionary that represents a playing board
    :raises: TypeError: if rows, columns, or floors is not an integer
    :raises: ValueError: if rows, columns is not a positive integer more than or equal to two
    :raises: ValueError: if floors is not a positive integer more than or equal to one
    """
    if type(rows) is not int or type(columns) is not int or type(floors) is not int:
        raise TypeError("Board can't be initialized. Arguments should be an integer.")
    elif rows < 2 or columns < 2:
        raise ValueError("Board can't be initialized. Rows and columns must be more than or equal to 2.")
    elif floors < 1:
        raise ValueError("Board can't be initialized. Floors must be more than or equal to 1.")
    else:
        list_of_descriptions = ["The air in the room is clear but cold. The room smells dank or moldy."
                                " A faint chanting noise can be heard.",
                                "Roughly chiseled into the corner of one wall are 42 small tally marks. "
                                "A desiccated naked human male corpse lies in one corner.",
                                "The air in the room is clear and warm. The room smells stale."
                                " A faint banging noise can be heard.",
                                "Painted with white, green, and black pigments is a well-drawn picture of two trolls"
                                " wielding large spiked maces. Five bodies lay fallen in a pile near one corner; two "
                                "human males, one female, a male dwarf, and a female elf. They appear to have died "
                                "in the ""last hour and have been thoroughly looted except for their clothes."]
        board = list(product(range(rows), range(columns), range(floors)))
        board = {index: list_of_descriptions[random.randint(0, len(list_of_descriptions)-1)] for index in board}
        add_bosses(board, rows, columns, floors)
        return board


def add_bosses(board: dict, rows: int, columns: int, floors: int) -> None:
    """
    Add bosses to the last room of each floor in board.

    :param board: a dictionary containing tuples of length 3 with positive integers as keys
    :param rows: a positive integer
    :param columns: a positive integer
    :param floors: a positive integer
    :precondition: board must contain at least four tuple keys of length three with positive integers
    :precondition: rows must be a positiver integer more than or equal to two
    :precondition: columns must be a positiver integer more than or equal to two
    :precondition: floors must be a positiver integer more than or equal to one
    :postcondition: applies bosses to the last room of each floor in board
    :raises: TypeError: if board is not a dictionary or rows, columns, and floors are not positive integers
    :raises: ValueError: if rows or columns are not positive integers more than or equal to two
    :raises: KeyError: if board does not contain a tuple with rows, columns, and floors as a key
    """
    if type(board) is not dict:
        raise TypeError("Must pass board as a dictionary.")
    elif type(rows) is not int or type(columns) is not int or type(floors) is not int:
        raise TypeError("Must pass rows columns and floors as a positive integer.")
    elif rows < 2 or columns < 2:
        raise ValueError("Rows and columns must be more than or equal to 2.")
    elif (rows-1, columns-1, floors-1) not in board:
        raise KeyError("Coordinates must exist within board.")
    else:
        for floor in range(floors):
            board[(rows-1, columns-1, floor)] = "BOSS HERE"
            board[(rows-2, columns-1, floor)] = "You feel an ominous presence coming from the door to the east.."
            board[(rows-1, columns-2, floor)] = "You feel an ominous presence coming from the door to the south.."


def main():
    """
    Drive the program.
    """
    print(make_board(4, 4, 2))


if __name__ == "__main__":
    main()
