from unittest import TestCase
from combat.game_combat import check_for_stun


class TestCheckForStun(TestCase):
    def test_check_for_stun_true(self):
        creep = {'Name': 'EYE OF CTHULHU', 'HP': 10, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': True, 'EXP': 100}
        expected = True
        self.assertEqual(expected, check_for_stun(creep))

    def test_check_for_stun_false(self):
        creep = {'Name': 'EYE OF CTHULHU', 'HP': 10, 'ATK': 25, 'Affliction': None, 'Turn': True, 'EXP': 100}
        expected = False
        self.assertEqual(expected, check_for_stun(creep))

    def test_check_for_stun_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            check_for_stun("Not a dictionary.")

    def test_check_for_stun_nonexistent_key(self):
        with self.assertRaises(KeyError):
            check_for_stun({"Not the key": 123})
