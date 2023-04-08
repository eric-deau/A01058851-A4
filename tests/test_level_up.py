from unittest import TestCase
from character.leveling import level_up


class TestLevelUp(TestCase):
    def test_level_up_successful_level_up(self):
        char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 100, 'Level': 1, 'Turn': False}
        level_up(char_one)
        self.assertEqual(2, char_one['Level'])

    def test_level_up_no_level_up(self):
        char_one = {'name': 'RAKSHASA', 'class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0, 'Y-coord': 0,
                    'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 80, 'Level': 1, 'Turn': False}
        level_up(char_one)
        self.assertEqual(1, char_one['Level'])

    def test_level_up_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            level_up("Not a dictionary.")

    def test_level_up_nonexistent_keys(self):
        with self.assertRaises(KeyError):
            level_up({"This is not the key": "Nope", "EXPERIENCE": "Still an error"})
