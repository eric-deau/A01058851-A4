from unittest import TestCase
from unittest.mock import patch
from combat.encounters import encounter_victory


class TestEncounterVictory(TestCase):
    @patch('random.randint', side_effect=[40, 40])
    def test_encounter_victory_no_level(self, _):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 50, 'Level': 2, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 0, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False,
                          'EXP': 25}
        encounter_victory(test_char_one, test_creep_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 340, 'MP': 240, 'EXP': 75, 'Level': 2, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    @patch('random.randint', side_effect=[40, 40])
    def test_encounter_victory_level_up(self, _):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 0,
                         'Y-coord': 0, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 50, 'Level': 1, 'Turn': False,
                         'Affliction': None}
        test_creep_one = {'Name': 'EYE OF CTHULHU', 'HP': 0, 'ATK': 25, 'Affliction': 'Bleed', 'Turn': False,
                          'EXP': 55}
        encounter_victory(test_char_one, test_creep_one)
        expected = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 90, 'Spell': 'Doomsday', 'X-coord': 0,
                    'Y-coord': 0, 'Z-coord': 0, 'HP': 540, 'MP': 320, 'EXP': 105, 'Level': 2, 'Turn': False,
                    'Affliction': None}
        self.assertEqual(expected, test_char_one)

    def test_encounter_victory_incorrect_data_types(self):
        with self.assertRaises(TypeError):
            encounter_victory("Something", "is nothing.")
