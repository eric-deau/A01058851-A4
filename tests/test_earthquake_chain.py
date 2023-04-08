from unittest import TestCase
from combat.abilities import earthquake_chain


class TestEarthquakeChain(TestCase):
    def test_earthquake_chain_enemy_slain(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain',
                         'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        earthquake_chain(test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -16.0, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_earthquake_chain_enemy_still_alive(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain',
                         'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        earthquake_chain(test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -54.0, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_earthquake_chain_invalid_data_type(self):
        with self.assertRaises(TypeError):
            earthquake_chain("Not a dictionary", "Another not a dictionary")

    def test_earthquake_chain_one_valid_one_invalid_data_type(self):
        with self.assertRaises(TypeError):
            earthquake_chain({}, "Another not a dictionary")

    def test_earthquake_chain_invalid_keys(self):
        with self.assertRaises(KeyError):
            earthquake_chain({"Health": 10}, {"HP": 20})

    def test_earthquake_chain_invalid_key_values(self):
        with self.assertRaises(ValueError):
            earthquake_chain({"Attack": -3}, {"HP": -2, "Affliction": None})

    def test_earthquake_chain_one_valid_one_invalid_key_value(self):
        with self.assertRaises(ValueError):
            earthquake_chain({"Attack": 50}, {"HP": -2, "Affliction": None})
