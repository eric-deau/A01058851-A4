from unittest import TestCase
from combat.encounters import win_guessing_game


class TestWinGuessingGame(TestCase):
    def test_win_guessing_game_high_hp(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        win_guessing_game(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 330.0, 'MP': 220.0, 'EXP': 222, 'Level': 2, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_win_guessing_game_lower_hp(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 20, 'MP': 100, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        win_guessing_game(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 22.0, 'MP': 110.0, 'EXP': 222, 'Level': 2, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_win_guessing_game_no_dict(self):
        with self.assertRaises(TypeError):
            win_guessing_game("Not a dictionary")

    def test_win_guessing_game_missing_keys(self):
        with self.assertRaises(KeyError):
            win_guessing_game({"HP": 10, "MP": 10})

    def test_win_guessing_game_wrong_keys(self):
        with self.assertRaises(KeyError):
            win_guessing_game({"Health": 10, "MP": 10, "Name": "olleH"})

    def test_win_guessing_game_wrong_value_hp(self):
        with self.assertRaises(ValueError):
            win_guessing_game({"HP": -10, "MP": 10, "Name": "olleH"})

    def test_win_guessing_game_wrong_value_MP(self):
        with self.assertRaises(ValueError):
            win_guessing_game({"HP": 10, "MP": -10, "Name": "olleH"})
