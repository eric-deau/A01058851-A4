from unittest import TestCase
from combat.afflictions import damage_over_time


class TestDamageOverTime(TestCase):
    def test_damage_over_time_burn(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Burn',
                          'Turn': False, 'EXP': 100}
        damage_over_time(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 25, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_damage_over_time_bleed(self):
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': 'Bleed',
                          'Turn': False, 'EXP': 100}
        damage_over_time(test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 15, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_damage_over_time_invalid_data_type(self):
        with self.assertRaises(TypeError):
            damage_over_time("Not a dictionary")

    def test_damage_over_time_missing_keys(self):
        with self.assertRaises(KeyError):
            damage_over_time({"Affliction": 'Burn'})

    def test_damage_over_time_incorrect_keys(self):
        with self.assertRaises(KeyError):
            damage_over_time({"Afflictions": 'Burn', 'Health': 50})
