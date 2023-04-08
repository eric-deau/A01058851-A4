from unittest import TestCase
from utilities.game_checks import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_correct_coordinates(self):
        example_char_one = {'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, "HP": 2}
        self.assertEqual(True, check_if_goal_attained(example_char_one, 4, 4, 3))

    def test_check_if_goal_attained_false_coordinates(self):
        example_char_two = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, "HP": 2}
        self.assertEqual(False, check_if_goal_attained(example_char_two, 4, 4, 3))

    def test_check_if_goal_attained_hp_zero_correct_coordinates(self):
        example_char_three = {'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, "HP": 0}
        self.assertEqual(False, check_if_goal_attained(example_char_three, 4, 4, 3))

    def test_check_if_goal_attained_hp_zero_incorrect_coordinates(self):
        example_char_four = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, "HP": 0}
        self.assertEqual(False, check_if_goal_attained(example_char_four, 4, 4, 3))
