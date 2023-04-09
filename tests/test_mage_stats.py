from unittest import TestCase
from character.character_creation import mage_stats


class TestMageStats(TestCase):
    def test_mage_stats(self):
        test_char_three = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': None, 'Spell': 'Doomsday', 'MP Cost': None,
                           'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1,
                           'Turn': False, 'Affliction': None}
        mage_stats(test_char_three)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 35, 'Spell': 'Doomsday', 'MP Cost': None,
                    'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 90, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_three)

    def test_mage_stats_incorrect_type(self):
        with self.assertRaises(TypeError):
            mage_stats("Not a dictionary")
