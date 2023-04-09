import io
from unittest import TestCase
from unittest.mock import patch
from character.display_status import display_status


class TestDisplayStatus(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Y"])
    def test_display_status_user_displays_status(self, _, mock_output):
        test_char = {'Affliction': None, 'Attack': 30, 'Class': 'Warrior', 'EXP': 0, 'HP': 80, 'Level': 1, 'MP': 150,
                     'MP Cost': None, 'Name': 'Bobby B', 'Spell': 'Doomsday', 'Turn': False, 'X-coord': 0, 'Y-coord': 0,
                     'Z-coord': 0}
        expected = "Here is your status for Bobby B\nAffliction: None\nClass: Warrior\nEXP: 0\n" \
                   "HP: 80\nLevel: 1\nMP: 150\nName: Bobby B\n"
        display_status(test_char)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["No"])
    def test_display_status_no_display(self, _):
        test_char = {'Affliction': None, 'Attack': 30, 'Class': 'Thief', 'EXP': 0, 'HP': 80, 'Level': 1, 'MP': 150,
                     'MP Cost': None, 'Name': 'Bobby B', 'Spell': 'Doomsday', 'Turn': False, 'X-coord': 0, 'Y-coord': 0,
                     'Z-coord': 0}
        expected = None
        self.assertEqual(expected, display_status(test_char))

    def test_display_status_invalid_data_type(self):
        with self.assertRaises(TypeError):
            display_status("Not a dictionary.")
