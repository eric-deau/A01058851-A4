from unittest import TestCase
from unittest.mock import patch
from combat.game_combat import get_attack_choice


class TestGetAttackChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_attack_choice_regular_attack(self, _):
        test_char_one = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        actual = get_attack_choice(test_char_one)
        expected = '1'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_attack_choice_spell(self, _):
        test_char_one = {'Name': 'Bob', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        actual = get_attack_choice(test_char_one)
        expected = '2'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_attack_choice_run_away(self, _):
        test_char_one = {'Name': 'Carlo', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        actual = get_attack_choice(test_char_one)
        expected = '3'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['hi', 'hi', 'hi', 'hi', '3'])
    def test_get_attack_choice_multiple_invalid_inputs(self, _):
        test_char_one = {'Name': 'Carl', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        actual = get_attack_choice(test_char_one)
        expected = '3'
        self.assertEqual(expected, actual)
