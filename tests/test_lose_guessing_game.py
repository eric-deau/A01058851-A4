from unittest import TestCase
from combat.encounters import lose_guessing_game


class TestLoseGuessingGame(TestCase):
    def test_lose_guessing_game(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        lose_guessing_game(test_char, '4', '2')
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'X-coord': 3, 'Y-coord': 3,
                    'Z-coord': 2, 'HP': 72.0, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char)

    def test_lose_guessing_game_higher_hp(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 300, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': 'Coward'}
        lose_guessing_game(test_char, '4', '2')
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 270.0, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': 'Coward'}
        self.assertEqual(expected, test_char)

    def test_lose_guessing_game_no_dict(self):
        with self.assertRaises(TypeError):
            lose_guessing_game("Not a dictionary", '2', '3')

    def test_lose_guessing_game_no_str(self):
        with self.assertRaises(TypeError):
            lose_guessing_game({}, 2, 3)

    def test_lose_guessing_game_no_dict(self):
        with self.assertRaises(ValueError):
            lose_guessing_game({}, '2', 'Word')
