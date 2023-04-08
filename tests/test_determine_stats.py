from unittest import TestCase
from character.character_creation import determine_stats


class TestDetermineStats(TestCase):
    def test_determine_stats_mage(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': None, 'Spell': 'Doomsday', 'MP Cost': None,
                         'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        determine_stats(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None,
                    'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_determine_stats_warrior(self):
        test_char_two = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': None, 'Spell': 'Earthquake Chain',
                         'MP Cost': None, 'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0,
                         'Level': 1, 'Turn': False, 'Affliction': None}
        determine_stats(test_char_two)
        expected = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 50, 'Spell': 'Earthquake Chain',
                    'MP Cost': None, 'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 110, 'MP': 50, 'EXP': 0,
                    'Level': 1, 'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_two)

    def test_determine_stats_thief(self):
        test_char_three = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': None, 'Spell': 'Stab', 'MP Cost': None,
                           'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1,
                           'Turn': False, 'Affliction': None}
        determine_stats(test_char_three)
        expected = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 40, 'Spell': 'Stab', 'MP Cost': None,
                    'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, 'HP': 90, 'MP': 100, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_three)

    def test_determine_stats_incorrect_type(self):
        with self.assertRaises(TypeError):
            determine_stats("Not a dictionary")

    def test_determine_stats_invalid_key(self):
        with self.assertRaises(KeyError):
            determine_stats({"Not the key you are looking for": "No sir."})

    def test_determine_stats_invalid_value(self):
        with self.assertRaises(ValueError):
            determine_stats({"Class": 43110})
