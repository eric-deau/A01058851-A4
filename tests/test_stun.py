from unittest import TestCase
from combat.afflictions import stun


class TestStun(TestCase):
    def test_stun(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': True,
                          'EXP': 100}
        stun(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False,
                    'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_stun_invalid_data_type(self):
        with self.assertRaises(TypeError):
            stun("Not a dictionary")

    def test_stun_missing_keys(self):
        with self.assertRaises(KeyError):
            stun({"NotTurn": False})

    def test_stun_incorrect_affliction_value(self):
        with self.assertRaises(ValueError):
            stun({"Turn": False, 'Affliction': 'Burn'})
