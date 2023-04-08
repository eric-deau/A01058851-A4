from unittest import TestCase
from movement.movement import check_for_floor_change


class TestCheckForFloorChange(TestCase):
    def test_check_for_floor_change_no_change(self):
        example_character_one = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        check_for_floor_change(example_character_one, 3, 3, 3)
        expected = {"X-coord": 1, "Y-coord": 0, "Z-coord": 0, "HP": 2}
        self.assertEqual(expected, example_character_one)

    def test_check_for_floor_change_change_level(self):
        example_character_one = {"X-coord": 2, "Y-coord": 2, "Z-coord": 0, "HP": 2}
        check_for_floor_change(example_character_one, 3, 3, 3)
        expected = {"X-coord": 0, "Y-coord": 0, "Z-coord": 1, "HP": 2}
        self.assertEqual(expected, example_character_one)

    def test_check_for_floor_no_dictionary(self):
        with self.assertRaises(TypeError):
            check_for_floor_change("Not a dictionary", 2, 2, 3)

    def test_check_for_floor_no_integer(self):
        with self.assertRaises(TypeError):
            check_for_floor_change({}, 2.23, 2, 3)

    def test_check_for_floor_incorrect_rows_and_columns(self):
        with self.assertRaises(ValueError):
            check_for_floor_change({"X-coord": 2, "Y-coord": 2, "Z-coord": 0, "HP": 2}, 1, 1, 3)

    def test_check_for_floor_incorrect_floors(self):
        with self.assertRaises(ValueError):
            check_for_floor_change({"X-coord": 2, "Y-coord": 2, "Z-coord": 0, "HP": 2}, 3, 3, 0)
