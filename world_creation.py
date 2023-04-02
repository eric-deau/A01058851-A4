import random


def make_board(rows, columns, floors):
    list_of_descriptions = ["The air in the room is clear but cold. The room smells dank or moldy."
                            " A faint chanting noise can be heard.",
                            "Roughly chiseled into the corner of one wall are 42 small tally marks. "
                            "A desiccated naked human male corpse lies in one corner.",
                            "The air in the room is clear and warm. The room smells stale."
                            " A faint banging noise can be heard.",
                            "Painted with white, green, and black pigments is a well-drawn picture of two trolls"
                            " wielding large spiked maces. Five bodies lay fallen in a pile near one corner; two "
                            "human males, one female, a male dwarf, and a female elf. They appear to have died in the "
                            "last hour and have been thoroughly looted except for their clothes."]
    board = {(row, column, floor): list_of_descriptions[random.randint(0, len(list_of_descriptions)-1)]
             for row in range(rows) for column in range(columns) for floor in range(floors)}
    first_floor_descriptions(board)
    second_floor_descriptions(board)
    third_floor_descriptions(board)
    print(board)
    return board


def first_floor_descriptions(board):
    board[(3, 4, 0)] = "You feel an evil presence watching you.."
    board[(4, 3, 0)] = "The air is getting colder around you.."
    board[(4, 4, 0)] = "Eye of Cthulhu blocks the staircase to another floor."


def second_floor_descriptions(board):
    board[(3, 4, 1)] = "There is noise coming from the door to the east.."
    board[(4, 3, 1)] = "There is noise coming from the door to the south.."
    board[(4, 4, 1)] = "A treasure chest, and a staircase to another floor."


def third_floor_descriptions(board):
    board[(3, 4, 2)] = "You feel an ominous presence coming from the door to the east.."
    board[(4, 3, 2)] = "You feel an ominous presence coming from the door to the south.."
    board[(4, 4, 2)] = "Zakum, the evil spirit is blocking the exit to this place!"


def main():
    print("Hello World")
    make_board(5, 5, 3)


if __name__ == "__main__":
    main()
