from unittest import TestCase
from combat.abilities import run_away


class TestRunAway(TestCase):
    def test_run_away_cast_run_away(self):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None,
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        run_away(test_char)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 30, 'Spell': 'Doomsday', 'MP Cost': None,
                    'X-coord': 0, 'Y-coord': 0, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                    'Turn': False, 'Affliction': 'Coward'}
        self.assertEqual(expected, test_char)

    def test_run_away_incorrect_argument_type(self):
        with self.assertRaises(TypeError):
            run_away("How come I keep passing strings as my example?")

    def test_run_away_nonexistent_keys(self):
        with self.assertRaises(KeyError):
            run_away({"NotAffliction": None})

    def test_run_away_incorrect_x_z_value(self):
        with self.assertRaises(ValueError):
            run_away({'X-coord': -2, 'Y-coord': 0, 'Z-coord': -1, 'Affliction': None})

    def test_run_away_incorrect_coordinate_values(self):
        with self.assertRaises(ValueError):
            run_away({'X-coord': -2, 'Y-coord': 0, 'Z-coord': -1, 'Affliction': None})

    def test_run_away_all_incorrect_coordinates(self):
        with self.assertRaises(ValueError):
            run_away({'X-coord': -2, 'Y-coord': -3, 'Z-coord': -1, 'Affliction': None})
