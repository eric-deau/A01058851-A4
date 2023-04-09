from unittest import TestCase
from unittest.mock import patch
from combat.encounters import guessing_game


class TestGuessingGame(TestCase):
    @patch('builtins.input', return_value="4")
    @patch('random.randint', side_effect=[2])
    def test_guessing_game_incorrect_answer_number(self, _, __):
        test_char = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        guessing_game(test_char)
        expected = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 72.0, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char)

    @patch('builtins.input', return_value="2")
    @patch('random.randint', side_effect=[2])
    def test_guessing_game_correct_answer(self, _, __):
        test_char = {'Name': 'NOTRAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        guessing_game(test_char)
        expected = {'Name': 'NOTRAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 88.0, 'MP': 165.0, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char)

    def test_guessing_game_invalid_data_type(self):
        with self.assertRaises(TypeError):
            guessing_game("Not a dictionary")

    def test_guessing_game_missing_key(self):
        with self.assertRaises(KeyError):
            guessing_game({"Health": 0.2})

    def test_guessing_game_invalid_hp_value(self):
        with self.assertRaises(ValueError):
            guessing_game({"HP": -4})
