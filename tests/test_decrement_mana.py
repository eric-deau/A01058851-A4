from unittest import TestCase
from combat.abilities import decrement_mana


class TestDecrementMana(TestCase):
    def test_decrement_mana_doomsday(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                         'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        decrement_mana(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 30, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_decrement_mana_earthquake_chain(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain',
                         'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        decrement_mana(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 80, 'Spell': 'Earthquake Chain',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 50, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_decrement_mana_stab(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 80, 'Spell': 'Stab',
                         'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 80, 'EXP': 0, 'Level': 1,
                         'Turn': False, 'Affliction': None}
        decrement_mana(test_char_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 80, 'Spell': 'Stab',
                    'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 110, 'MP': 50, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_decrement_mana_invalid_data_type(self):
        with self.assertRaises(TypeError):
            decrement_mana("Not a dictionary")

    def test_decrement_mana_invalid_key(self):
        with self.assertRaises(KeyError):
            decrement_mana({"Mana": 10})

    def test_decrement_mana_invalid_key_values(self):
        with self.assertRaises(ValueError):
            decrement_mana({'MP': -10, 'Spell': "NotStab"})

    def test_decrement_mana_one_valid_one_invalid_key_value(self):
        with self.assertRaises(ValueError):
            decrement_mana({"MP": 50, "Spell": "NotStab"})
