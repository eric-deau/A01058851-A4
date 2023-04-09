import time


def beginning_of_game():
    """
    Print the starting lore of the game in a rolling text.

    :postcondition: displays a slow rolling text in the console to users
    """
    with open('board/beginning.txt', 'r') as file_object:
        content = file_object.read()
    for line in content:
        print(line, end="")
        time.sleep(.10)
    print()


def main():
    beginning_of_game()


if __name__ == "__main__":
    main()
