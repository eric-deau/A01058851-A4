from unittest import TestCase
from character.leveling import level_two


class TestLevelTwo(TestCase):
    def test_level_two_invalid_type(self):
        with self.assertRaises(TypeError):
            level_two("Not a dictionary.")

    def test_level_two_invalid_keys(self):
        with self.assertRaises(KeyError):
            level_two({"Not a dictionary.": "Definitely not existing keys"})

    def test_level_two_invalid_values(self):
        with self.assertRaises(ValueError):
            level_two({"Level": 2, "Attack": -2, "HP": -199, "MP": -239.2})

    def test_level_two_level_up(self):
        char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 100, 'Level': 1, 'Turn': False}
        level_two(char_one)
        self.assertEqual({'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                          'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 180, 'EXP': 100, 'Level': 2, 'Turn': False},
                         char_one)
