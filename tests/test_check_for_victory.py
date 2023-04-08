from unittest import TestCase
from combat.encounters import check_for_victory


class TestCheckForVictory(TestCase):
    def test_check_for_victory_victorious(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 0, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False,
                          'EXP': 100}
        expected = True
        self.assertEqual(expected, check_for_victory(test_char_one, test_creep_one))

    def test_check_for_victory_not_victorious(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False,
                          'EXP': 100}
        expected = False
        self.assertEqual(expected, check_for_victory(test_char_one, test_creep_one))

    def test_check_for_victory_incorrect_data_types(self):
        with self.assertRaises(TypeError):
            check_for_victory("not a dictionary", "definitely not a dictionary")

    def test_check_for_victory_one_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            check_for_victory({}, "definitely not a dictionary")

    def test_check_for_victory_one_missing_key(self):
        with self.assertRaises(KeyError):
            check_for_victory({"NotHP": 2}, {"HP": 2})

    def test_check_for_victory_both_missing_key(self):
        with self.assertRaises(KeyError):
            check_for_victory({"NotHP": 2}, {"MissingHP": 2})
