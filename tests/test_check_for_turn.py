from unittest import TestCase
from combat.encounters import check_for_turn


class TestCheckForTurn(TestCase):
    def test_check_for_turn_false(self):
        test_char_one = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = False
        self.assertEqual(expected, check_for_turn(test_char_one))

    def test_check_for_turn_true(self):
        test_char_one = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                         'Affliction': None}
        expected = True
        self.assertEqual(expected, check_for_turn(test_char_one))

    def test_check_for_turn_invalid_data_type(self):
        with self.assertRaises(TypeError):
            check_for_turn("Not a dictionary.")

    def test_check_for_turn_no_turn_key(self):
        with self.assertRaises(KeyError):
            check_for_turn({"NotTurn": False})

    def test_check_for_turn_invalid_key_value_type(self):
        with self.assertRaises(TypeError):
            check_for_turn({"Turn": None})

