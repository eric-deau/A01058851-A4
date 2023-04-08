from unittest import TestCase
from unittest.mock import patch
from character.character_creation import choose_class


class TestChooseClass(TestCase):

    @patch('builtins.input', side_effect=["1", "Y"])
    def test_choose_class_warrior(self, _):
        actual = choose_class()
        expected = "Warrior"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3", "Y"])
    def test_choose_class_thief(self, _):
        actual = choose_class()
        expected = "Thief"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2", "Y"])
    def test_choose_class_mage(self, _):
        actual = choose_class()
        expected = "Mage"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2", "NO NOT THAT ONE", "3", "y"])
    def test_choose_class_reselect_class(self, _):
        actual = choose_class()
        expected = "Thief"
        self.assertEqual(expected, actual)
