import time


def slow_rolling_text_printer(input_file):
    """
    Print the starting lore of the game in a rolling text.

    :postcondition: displays a slow rolling text in the console to users
    :raises: FileNotFoundError: if file does not exist in directory named board
    """
    with open(input_file, 'r') as file_object:
        content = file_object.read()
    for line in content:
        print(f"{line}", end="")
        time.sleep(.10)
    print()


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
