from unittest import TestCase
from unittest.mock import patch
from utilities.game_checks import defeat
import io


class TestDefeat(TestCase):

    def test_defeat_file_non_existent(self):
        with self.assertRaises(FileNotFoundError):
            defeat("not a file")

    @patch('builtins.open', return_value=io.StringIO('Hello'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_beginning_of_game(self, mock_output, _):
        defeat('test_slow_rolling_text_printer.py')
        expected = 'Hello\n'
        self.assertEqual(mock_output.getvalue(), expected)
