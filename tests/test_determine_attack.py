from unittest import TestCase
from combat.game_combat import determine_attack


class TestDetermineAttack(TestCase):

    def test_determine_attack_invalid_data_type_creep_character(self):
        with self.assertRaises(TypeError):
            determine_attack('1', [], [])

    def test_determine_attack_invalid_data_type_dicts(self):
        with self.assertRaises(TypeError):
            determine_attack(43110, {}, {})

    def test_determine_attack_regular_attack(self):
        test_char_one = {'Name': 'bob', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        determine_attack('Attack', test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 10, 'ATK': 25, 'Affliction': None, 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    def test_determine_attack_spell(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        determine_attack('Spell', test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -32.0, 'ATK': 25, 'Affliction': 'Burn', 'Turn': False, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)
