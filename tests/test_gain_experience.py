from unittest import TestCase
from character.leveling import gain_experience


class TestGainExperience(TestCase):
    def test_gain_experience_invalid_data_type(self):
        with self.assertRaises(TypeError):
            gain_experience("Not a dictionary", "Also not a dictionary.")

    def test_gain_experience_nonexistent_key(self):
        with self.assertRaises(KeyError):
            gain_experience({"Not a dictionary": "Also not a dictionary."}, {"Not a dictionary": "A."})

    def test_gain_experience_incorrect_values(self):
        with self.assertRaises(ValueError):
            gain_experience({"EXP": -1}, {"EXP": -2})

    def test_gain_experience_zero_exp(self):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0,
                              'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 0, 'Level': 1, 'Turn': False}
        test_mob_one = {'Name': 'Slime', 'HP': 0, 'ATK': 10, 'Affliction': None, 'EXP': 10}
        gain_experience(test_char_one, test_mob_one)
        self.assertEqual(10, test_char_one['EXP'])

    def test_gain_experience_some_exp(self):
        test_char_two = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday', 'X-coord': 0,
                              'Y-coord': 0, 'Z-coord': 0, 'HP': 100, 'MP': 100, 'EXP': 50, 'Level': 1, 'Turn': False}
        test_mob_two = {'Name': 'Slime', 'HP': 10, 'ATK': 10, 'Affliction': None, 'EXP': 30}
        gain_experience(test_char_two, test_mob_two)
        self.assertEqual(80, test_char_two['EXP'])
