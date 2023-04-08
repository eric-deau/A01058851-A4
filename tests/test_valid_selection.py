from unittest import TestCase
from unittest.mock import patch
from character.character_creation import valid_selection


class TestValidSelection(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_valid_selection_initial_invalid_choice(self, _):
        actual = valid_selection("6", {'1': 'Warrior', '2': 'Mage', '3': 'Thief'})
        expected = "Warrior"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[])
    def test_valid_selection_initial_valid_choice(self, _):
        actual = valid_selection("2", {'1': 'Warrior', '2': 'Mage', '3': 'Thief'})
        expected = "Mage"
        self.assertEqual(expected, actual)

    def test_valid_selection_not_string_dict(self):
        with self.assertRaises(TypeError):
            valid_selection(43110, {})

    def test_valid_selection_string_not_dict(self):
        with self.assertRaises(TypeError):
            valid_selection("Hello", [])

    def test_valid_selection_invalid_keys(self):
        with self.assertRaises(KeyError):
            valid_selection("2", {"One": "W", "Two": "M"})
