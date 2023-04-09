from unittest import TestCase
from utilities.game_checks import reset_affliction


class TestResetAffliction(TestCase):
    def test_reset_affliction_reset_affliction(self):
        char_one = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2, 'Affliction': 'Coward'}
        reset_affliction(char_one)
        expected = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2, 'Affliction': None}
        self.assertEqual(expected, char_one)

    def test_reset_affliction_no_reset(self):
        char_one = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2, 'Affliction': None}
        reset_affliction(char_one)
        expected = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2, 'Affliction': None}
        self.assertEqual(expected, char_one)

    def test_reset_affliction_wrong_data_type(self):
        with self.assertRaises(TypeError):
            reset_affliction("Not a dictionary.")

    def test_reset_affliction_missing_key(self):
        with self.assertRaises(KeyError):
            reset_affliction({'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2})
