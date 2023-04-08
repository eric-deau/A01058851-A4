from unittest import TestCase
from unittest.mock import patch
from combat.encounters import determine_first_engage


class TestDetermineFirstEngage(TestCase):

    @patch('random.randint', return_value=1)
    def test_determine_first_engage_player_true(self, _):
        test_char_one = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        determine_first_engage(test_char_one, test_creep_one)
        expected = {'Name': 'Bobby', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                    'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    @patch('random.randint', return_value=2)
    def test_determine_first_engage_creep_true(self, _):
        test_char_one = {'Name': 'Rob', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        determine_first_engage(test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                    'Turn': True, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_determine_first_engage_invalid_data_type(self):
        with self.assertRaises(TypeError):
            determine_first_engage("Not a dictionary.", 34)

    def test_determine_first_engage_missing_turn_key(self):
        with self.assertRaises(KeyError):
            determine_first_engage({"Not a dictionary.": 34}, {'Turn': False})

    def test_determine_first_engage_invalid_key_type(self):
        with self.assertRaises(TypeError):
            determine_first_engage({"Turn": 34}, {'Turn': False})
