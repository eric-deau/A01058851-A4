from unittest import TestCase
from movement.movement import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_is_not_valid_Y_coords_up(self):
        test_character_one = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '1',
                          (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                          (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_one = "North Door"
        self.assertEqual(False, validate_move(test_board_one, test_character_one, test_direction_one))

    def test_validate_move_is_not_valid_Y_coords_down(self):
        test_character_two = {"X-coord": 0, "Y-coord": 1, "Z-coord": 0, "HP": 2}
        test_board_two = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '2',
                          (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                          (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_two = "South Door"
        self.assertEqual(False, validate_move(test_board_two, test_character_two, test_direction_two))

    def test_validate_move_is_not_valid_X_coords_left(self):
        test_character_three = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_three = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '3',
                            (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                            (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_three = "West Door"
        self.assertEqual(False, validate_move(test_board_three, test_character_three, test_direction_three))

    def test_validate_move_is_not_valid_X_coords_right(self):
        test_character_four = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_four = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '4',
                           (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                           (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_four = "East Door"
        self.assertEqual(False, validate_move(test_board_four, test_character_four, test_direction_four))

    def test_validate_move_is_valid_X_coords_right(self):
        test_character_five = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_five = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '5',
                           (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                           (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_five = "East Door"
        self.assertEqual(True, validate_move(test_board_five, test_character_five, test_direction_five))

    def test_validate_move_is_valid_X_coords_left(self):
        test_character_six = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_six = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '6',
                          (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                          (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_six = "West Door"
        self.assertEqual(True, validate_move(test_board_six, test_character_six, test_direction_six))

    def test_validate_move_is_valid_Y_coords_down(self):
        test_character_seven = {"X-coord": 0, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        test_board_seven = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '7',
                            (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                            (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_seven = "South Door"
        self.assertEqual(True, validate_move(test_board_seven, test_character_seven, test_direction_seven))

    def test_validate_move_is_valid_Y_coords_up(self):
        test_character_eight = {"X-coord": 0, "Y-coord": 1, "Z-coord": 0, "HP": 2}
        test_board_eight = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '8',
                            (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                            (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_eight = "North Door"
        self.assertEqual(True, validate_move(test_board_eight, test_character_eight, test_direction_eight))

    def test_validate_move_is_valid_different_Z_coord(self):
        test_character_nine = {"X-coord": 0, "Y-coord": 1, "Z-coord": 1, "HP": 2}
        test_board_nine = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): '9',
                           (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                           (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        test_direction_eight = "North Door"
        self.assertEqual(True, validate_move(test_board_nine, test_character_nine, test_direction_eight))

