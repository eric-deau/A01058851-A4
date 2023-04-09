from unittest import TestCase
from unittest.mock import patch
from utilities.lore import slow_rolling_text_printer
import io


class TestBeginningOfGame(TestCase):

    def test_beginning_of_game_file_non_existent(self):
        with self.assertRaises(FileNotFoundError):
            slow_rolling_text_printer("not a file")

    @patch('builtins.open', return_value=io.StringIO('Hello'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_beginning_of_game(self, mock_output, _):
        slow_rolling_text_printer('test_slow_rolling_text_printer.py')
        expected = 'Hello\n'
        self.assertEqual(mock_output.getvalue(), expected)
