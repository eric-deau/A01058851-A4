from unittest import TestCase
from movement.movement import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_x_right_direction(self):
        example_character_one = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        example_direction_one = "East Door"
        move_character(example_character_one, example_direction_one)
        self.assertEqual({"X-coord": 2, "Y-coord": 0, "Z-coord": 0, "HP": 2}, example_character_one)

    def test_move_character_x_left_direction(self):
        example_character_two = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        example_direction_two = "West Door"
        move_character(example_character_two, example_direction_two)
        self.assertEqual({"X-coord": 0, "Y-coord": 0, "Z-coord": 0, "HP": 2}, example_character_two)

    def test_move_character_y_up_direction(self):
        example_character_three = {"X-coord": 1, "Y-coord": 1, "Z-coord": 0, "HP": 2}
        example_direction_three = "North Door"
        move_character(example_character_three, example_direction_three)
        self.assertEqual({"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}, example_character_three)

    def test_move_character_y_down_direction(self):
        example_character_four = {"X-coord": 1, "Y-coord": 1, "Z-coord": 0, "HP": 2}
        example_direction_four = "South Door"
        move_character(example_character_four, example_direction_four)
        self.assertEqual({"X-coord": 1, "Y-coord": 2, "Z-coord": 0, "HP": 2}, example_character_four)

    def test_move_character_different_z(self):
        example_character_four = {"X-coord": 1, "Y-coord": 1, "Z-coord": 1, "HP": 2}
        example_direction_four = "South Door"
        move_character(example_character_four, example_direction_four)
        self.assertEqual({"X-coord": 1, "Y-coord": 2, "Z-coord": 1, "HP": 2}, example_character_four)


