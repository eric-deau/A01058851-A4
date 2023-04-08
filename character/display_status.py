import time


def display_status(character):
    """
    Display the characteristics of a character.

    :param character: a dictionary
    :precondition: character must be a dictionary containing 'Name', 'Class', 'HP', 'MP', 'Level', 'EXP' and
                    'Affliction'
    :postcondition: prints the relevant characteristics of a character
    :raises: TypeError: if character is not a dictionary
    """
    if type(character) is not dict:
        raise TypeError("Must pass a dictionary as an argument.")
    else:
        status_check = input("Would you like to see your status? Type 'Y' to check,"
                             " else type anything else to proceed.")
        if status_check.lower() == "y":
            attributes = ('Name', 'Class', 'HP', 'MP', 'EXP', 'Level', 'Affliction')
            print(f"Here is your status for {character['Name']}")
            for key, value in character.items():
                if key in attributes:
                    print(f"{key}: {value}")
                    time.sleep(1)
        else:
            return


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
