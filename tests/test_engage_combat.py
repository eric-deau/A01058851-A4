from unittest import TestCase
from unittest.mock import patch
from combat.encounters import engage_combat


class TestEngageCombat(TestCase):
    @patch('builtins.input', side_effect=['3', '2'])
    @patch('random.randint', side_effect=[1, 3])
    def test_engage_combat_run_away(self, _, __):
        test_char_one = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        engage_combat(test_char_one, test_creep_one)
        expected = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 270.0, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                    'Affliction': 'Coward'}
        self.assertEqual(expected, test_char_one)

    @patch('builtins.input', side_effect=['1', '1', '1'])
    @patch('random.randint', side_effect=[1, 40, 40])
    def test_engage_combat_regular_attacks(self, _, __):
        test_char_one = {'Name': 'Someone', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        engage_combat(test_char_one, test_creep_one)
        expected = {'Name': 'Someone', 'Class': 'Mage', 'Attack': 110, 'Spell': 'Doomsday', 'X-coord': 3,
                    'Y-coord': 3, 'Z-coord': 0, 'HP': 690, 'MP': 365, 'EXP': 322, 'Level': 3, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', side_effect=[1, 40, 40])
    def test_engage_combat_spells(self, _, __):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 30, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        engage_combat(test_char_one, test_creep_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 110, 'Spell': 'Doomsday', 'X-coord': 3,
                    'Y-coord': 3, 'Z-coord': 0, 'HP': 690, 'MP': 315, 'EXP': 322, 'Level': 3, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', side_effect=[1, 40, 40])
    def test_engage_combat_death(self, _, __):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                         'Y-coord': 3, 'Z-coord': 0, 'HP': 20, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 230, 'ATK': 25, 'Affliction': None,
                          'Turn': False, 'EXP': 100}
        engage_combat(test_char_one, test_creep_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 3,
                    'Y-coord': 3, 'Z-coord': 0, 'HP': -5, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': True,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)
