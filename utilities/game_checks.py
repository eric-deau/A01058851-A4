import random


def check_if_goal_attained(current_character: dict) -> bool:
    """
    Check if a character meets the win condition of the game.

    :param current_character: a dictionary containing keys 'X-coordinates', 'Y-coordinates', and 'HP'
    :precondition: current_character must contain keys 'X-coordinates' and 'Y-coordinates' and 'HP'
    :precondition: current_character key 'HP' value must be a positive integer more than 0
    :precondition: current_character keys 'X-coordinates' value must be a positive integer more than 0
    :precondition: current_character keys 'Y-coordinates' value must be a positive integer more than 0
    :postcondition: determines if current_character meets the win condition of the game
    :return: a boolean value representing the win condition of the character

    >>> test_char_one = {'X-coordinates': 1, 'Y-coordinates': 1, 'HP': 2}
    >>> check_if_goal_attained(test_char_one)
    False

    >>> test_char_two = {'X-coordinates': 2, 'Y-coordinates': 2, 'HP': 2}
    >>> check_if_goal_attained(test_char_two)
    True
    """
    if current_character["X-coordinates"] and current_character["Y-coordinates"] == 4 and current_character['HP'] > 0:
        return True
    return False


def check_for_random_foes() -> int:
    """
    Determine if a character will have an encounter in the playing board 25% of the time.

    :postcondition: determines if a mini-game will be initialized 25% of the time
    :return: a boolean value representing if a foe is encountered 25% of the time
    """
    return random.randint(1, 4) == 1


def check_for_boss(character):
    if character['X-coord'] == 4 and character['Y-coord'] == 4:
        return True
    else:
        return False


def check_character_level(character, creep):
    if character['Level'] < creep['Level']:
        creep['ATK'] += 30
    else:
        creep['ATK'] -= 10


