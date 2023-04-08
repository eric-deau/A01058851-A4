from unittest import TestCase
from combat.game_combat import validate_attack_choice


class TestValidateAttackChoice(TestCase):
    def test_validate_attack_choice_true(self):
        test_char_one = {'Name': 'Bobby B', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
        expected = True
        self.assertEqual(expected, validate_attack_choice('1', character=test_char_one, choices=choices))

    def test_validate_attack_choice_false_not_a_choice(self):
        test_char_one = {'Name': 'BoB', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
        expected = False
        self.assertEqual(expected, validate_attack_choice('Not a choice', character=test_char_one, choices=choices))

    def test_validate_attack_choice_false_not_enough_mana(self):
        test_char_one = {'Name': 'BoB', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 0, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        choices = {'1': 'Attack', '2': 'Spell', '3': 'Run away'}
        expected = False
        self.assertEqual(expected, validate_attack_choice('2', character=test_char_one, choices=choices))

    def test_validate_attack_choice_invalid_selection_data_type(self):
        with self.assertRaises(TypeError):
            validate_attack_choice(123, {}, {})

    def test_validate_attack_choice_invalid_choices(self):
        with self.assertRaises(TypeError):
            validate_attack_choice(123, [], {})

    def test_validate_attack_choice_all_invalid(self):
        with self.assertRaises(TypeError):
            validate_attack_choice(123, [], "{}")
