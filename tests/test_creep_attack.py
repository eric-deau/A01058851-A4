from unittest import TestCase
from combat.game_combat import creep_attack


class TestCreepAttack(TestCase):

    def test_creep_attack_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            creep_attack("Not a dictionary", "Still not a dictionary")

    def test_creep_attack_valid_attack(self):
        test_char_one = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        creep_attack(test_char_one, test_creep_one)
        expected = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 275, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_creep_attack_creep_stunned(self):
        test_char_two = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_two = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': 'Stunned', 'Turn': False,
                          'EXP': 100}
        creep_attack(test_char_two, test_creep_two)
        expected = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                    'Affliction': None}
        self.assertEqual(expected, test_char_two)
