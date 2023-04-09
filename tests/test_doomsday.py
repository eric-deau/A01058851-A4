from unittest import TestCase
from combat.abilities import doomsday


class TestDoomsday(TestCase):
    def test_doomsday_enemy_slain(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        doomsday(test_char, test_creep)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -26.0, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep)

    def test_doomsday_enemy_still_alive(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        doomsday(test_char, test_creep)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 44.0, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep)

    def test_doomsday_invalid_data_type(self):
        with self.assertRaises(TypeError):
            doomsday("Not a dictionary", "Another not a dictionary")

    def test_doomsday_one_valid_one_invalid_data_type(self):
        with self.assertRaises(TypeError):
            doomsday({}, "Another not a dictionary")

    def test_doomsday_invalid_keys(self):
        with self.assertRaises(KeyError):
            doomsday({"Health": 10}, {"HP": 20})

    def test_doomsday_invalid_key_values(self):
        with self.assertRaises(ValueError):
            doomsday({"Attack": -3}, {"HP": -2, "Affliction": None})

    def test_doomsday_one_valid_one_invalid_key_value(self):
        with self.assertRaises(ValueError):
            doomsday({"Attack": 50}, {"HP": -2, "Affliction": None})
