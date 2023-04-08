from unittest import TestCase
from combat.game_combat import check_for_mana


class TestCheckForMana(TestCase):
    def test_check_for_mana_true_mage(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = True
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_false_mage(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Mage', 'Attack': 10, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 2, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = False
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_true_warrior(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Warrior', 'Attack': 10, 'Spell': 'Earthquake Chain', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = True
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_false_warrior(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Warrior', 'Attack': 10, 'Spell': 'Earthquake Chain', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 2, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = False
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_true_thief(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Thief', 'Attack': 10, 'Spell': 'Stab', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = True
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_false_thief(self):
        test_char_one = {'Name': 'ඞ', 'Class': 'Thief', 'Attack': 10, 'Spell': 'Stab', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 2, 'EXP': 222, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        expected = False
        self.assertEqual(expected, check_for_mana(test_char_one))

    def test_check_for_mana_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            check_for_mana("Not a dictionary.")
