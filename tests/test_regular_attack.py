from unittest import TestCase
from combat.abilities import regular_attack


class TestRegularAttack(TestCase):
    def test_regular_attack_enemy_still_alive(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 40, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        regular_attack(test_char, test_creep)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 60, 'ATK': 25, 'Affliction': None, 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep)

    def test_regular_attack_enemy_slain(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        regular_attack(test_char, test_creep)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -10.0, 'ATK': 25, 'Affliction': None, 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep)

    def test_regular_attack_invalid_data_type(self):
        with self.assertRaises(TypeError):
            regular_attack("Not a dictionary", "Another not a dictionary")

    def test_regular_attack_one_valid_one_invalid_data_type(self):
        with self.assertRaises(TypeError):
            regular_attack({}, "Another not a dictionary")

    def test_regular_attack_invalid_keys(self):
        with self.assertRaises(KeyError):
            regular_attack({"Health": 10}, {"HP": 20})

    def test_regular_attack_invalid_key_values(self):
        with self.assertRaises(ValueError):
            regular_attack({"Attack": -3}, {"HP": -2})

    def test_regular_attack_one_valid_one_invalid_key_value(self):
        with self.assertRaises(ValueError):
            regular_attack({"Attack": 50}, {"HP": -2})
