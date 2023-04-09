import time


def beginning_of_game():
    with open('board/beginning.txt', 'r') as file_object:
        content = file_object.read()
    # content = all_prefixes(content)
    for line in content:
        print(line, end="")
        time.sleep(.10)
    print()


def main():
    beginning_of_game()


if __name__ == "__main__":
    main()
