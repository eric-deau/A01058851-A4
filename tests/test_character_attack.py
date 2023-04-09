from unittest import TestCase
from unittest.mock import patch
from combat.game_combat import character_attack


class TestCharacterAttack(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_character_attack_regular_attack(self, _):
        test_char_one = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        character_attack(test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': 10, 'ATK': 25, 'Affliction': None, 'Turn': True, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    @patch('builtins.input', side_effect=['2'])
    def test_character_attack_spell(self, _):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        character_attack(test_char_one, test_creep_one)
        expected = {'Name': 'EYE OF CTHULHU', 'HP': -32.0, 'ATK': 25, 'Affliction': 'Burn', 'Turn': True, 'EXP': 100}
        self.assertEqual(expected, test_creep_one)

    @patch('builtins.input', side_effect=['3'])
    def test_character_run_away(self, _):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 4,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 20, 'ATK': 25, 'Affliction': None, 'Turn': False,
                          'EXP': 100}
        character_attack(test_char_one, test_creep_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                    'Affliction': 'Coward'}
        self.assertEqual(expected, test_char_one)
