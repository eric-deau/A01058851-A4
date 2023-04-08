from unittest import TestCase
from character.leveling import level_three


class TestLevelThree(TestCase):

    def test_level_three_invalid_type(self):
        with self.assertRaises(TypeError):
            level_three("Not a dictionary.")

    def test_level_three_invalid_keys(self):
        with self.assertRaises(KeyError):
            level_three({"Not a dictionary.": "Definitely not existing keys"})

    def test_level_three_invalid_values(self):
        with self.assertRaises(ValueError):
            level_three({"Level": 2, "Attack": -2, "HP": -199, "MP": -239.2})

    def test_level_three_level_up(self):
        char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 200, 'Level': 2, 'Turn': False}
        level_three(char_one)
        self.assertEqual({'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 90, 'Spell': 'Doomsday', 'X-coord': 0,
                          'Y-coord': 0, 'Z-coord': 0, 'HP': 450, 'MP': 225, 'EXP': 200, 'Level': 3, 'Turn': False},
                         char_one)
