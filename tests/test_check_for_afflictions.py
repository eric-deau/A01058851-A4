from unittest import TestCase
from combat.afflictions import check_for_creep_afflictions


class TestCheckForAfflictions(TestCase):
    def test_check_for_creep_afflictions_no_affliction(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, 'EXP': 100}
        check_for_creep_afflictions(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None, 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_check_for_creep_afflictions_burn(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Burn',
                          'Turn': False, 'EXP': 100}
        check_for_creep_afflictions(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 25, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_check_for_creep_afflictions_bleed(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Bleed',
                          'Turn': False, 'EXP': 100}
        check_for_creep_afflictions(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 15, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_check_for_creep_afflictions_stun(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned',
                          'Turn': True, 'EXP': 100}
        check_for_creep_afflictions(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_check_for_afflictions_invalid_data_type(self):
        with self.assertRaises(TypeError):
            check_for_creep_afflictions("Not a dictionary")

    def test_check_for_afflictions_nonexistent_key(self):
        with self.assertRaises(KeyError):
            check_for_creep_afflictions({"NotAffliction": 123})

    def test_check_for_afflictions_hp_no_affliction(self):
        with self.assertRaises(KeyError):
            check_for_creep_afflictions({"NotAffliction": 123, 'HP': 50})
