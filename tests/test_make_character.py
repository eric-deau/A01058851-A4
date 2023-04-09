from unittest import TestCase
from unittest.mock import patch
from character.character_creation import make_character


class TestMakeCharacter(TestCase):
    @patch('builtins.input', side_effect=["Bobby B", "Y", "2", "Y"])
    def test_make_character_all_correct_inputs(self, _):
        actual = make_character()
        expected = {'Affliction': None, 'Attack': 35, 'Class': 'Mage', 'EXP': 0, 'HP': 90, 'Level': 1, 'MP': 150,
                    'MP Cost': None, 'Name': 'Bobby B', 'Spell': 'Doomsday', 'Turn': False, 'X-coord': 0, 'Y-coord': 0,
                    'Z-coord': 0}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Bobby B", "NOPE", "AN ACTUAL NAME", "Y", "3", "NO", "1", "Y"])
    def test_make_character_some_incorrect_inputs(self, _):
        actual = make_character()
        expected = {'Affliction': None, 'Attack': 50, 'Class': 'Warrior', 'EXP': 0, 'HP': 110, 'Level': 1, 'MP': 50,
                    'MP Cost': None, 'Name': 'AN ACTUAL NAME', 'Spell': 'Earthquake Chain', 'Turn': False, 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0}
        self.assertEqual(expected, actual)
