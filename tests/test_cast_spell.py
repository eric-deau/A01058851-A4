import io
from unittest import TestCase
from unittest.mock import patch
from combat.abilities import cast_spell


class TestCastSpell(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_spell_earthquake_chain(self, mock_output):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Warrior', 'Attack': 70, 'Spell': 'Earthquake Chain',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 120, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        cast_spell(test_char, test_creep)
        expected = "Casting Earthquake Chain...\nEYE OF CTHULHU has been afflicted with Stunned!\nYou lost 30 MP.\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_spell_doomsday(self, mock_output):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 50, 'Spell': 'Doomsday',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 80, 'MP': 150, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        cast_spell(test_char, test_creep)
        expected = "Casting Doomsday...\nEYE OF CTHULHU has been afflicted with Burn!\nYou lost 60 MP.\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_spell_stab(self, mock_output):
        test_char = {'Name': 'RAKSHASA', 'Class': 'Thief', 'Attack': 40, 'Spell': 'Stab',
                     'X-coord': 3, 'Y-coord': 3, 'Z-coord': 2, 'HP': 90, 'MP': 100, 'EXP': 0, 'Level': 1,
                     'Turn': False, 'Affliction': None}
        test_creep = {'Name': 'EYE OF CTHULHU', 'HP': 100, 'ATK': 25, 'Affliction': None, 'Turn': False,
                      'EXP': 100}
        cast_spell(test_char, test_creep)
        expected = "Casting Stab...\nEYE OF CTHULHU has been afflicted with Bleed!\nYou lost 30 MP.\n"
        self.assertEqual(mock_output.getvalue(), expected)

    def test_cast_spell_invalid_data_type(self):
        with self.assertRaises(TypeError):
            cast_spell("Not a dictionary", "Another not a dictionary")

    def test_cast_spell_one_valid_one_invalid_data_type(self):
        with self.assertRaises(TypeError):
            cast_spell({}, "Another not a dictionary")

    def test_cast_spell_one_valid_one_invalid_key(self):
        with self.assertRaises(KeyError):
            cast_spell({"Health": 10}, {"HP": 20})

    def test_cast_spell_invalid_key_values(self):
        with self.assertRaises(ValueError):
            cast_spell({"Spell": "Kick"}, {"HP": -2})

    def test_cast_spell_one_valid_one_invalid_key_value(self):
        with self.assertRaises(ValueError):
            cast_spell({"Spell": "Stab"}, {"HP": -2})
