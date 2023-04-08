from unittest import TestCase
from character.character_creation import warrior_stats


class TestWarriorStats(TestCase):
    def test_warrior_stats(self):
        test_char_two = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': None, 'Spell': 'Earthquake Chain',
                         'MP Cost': None, 'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0,
                         'Level': 1, 'Turn': False, 'Affliction': None}
        warrior_stats(test_char_two)
        expected = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 50, 'Spell': 'Earthquake Chain',
                    'MP Cost': None, 'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 110, 'MP': 50, 'EXP': 0,
                    'Level': 1, 'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_two)

    def test_warrior_stats_incorrect_type(self):
        with self.assertRaises(TypeError):
            warrior_stats("Not a dictionary")
