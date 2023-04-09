from unittest import TestCase
from character.character_creation import thief_stats


class TestThiefStats(TestCase):
    def test_thief_stats(self):
        test_char_three = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': None, 'Spell': 'Stab', 'MP Cost': None,
                           'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1,
                           'Turn': False, 'Affliction': None}
        thief_stats(test_char_three)
        expected = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 60, 'Spell': 'Stab', 'MP Cost': None,
                    'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_three)

    def test_thief_stats_incorrect_type(self):
        with self.assertRaises(TypeError):
            thief_stats("Not a dictionary")
