from unittest import TestCase
from unittest.mock import patch
from utilities.game_checks import slow_print_by_line
import io


class TestSlowPrintByLine(TestCase):

    def test_slow_print_by_line_file_non_existent(self):
        with self.assertRaises(FileNotFoundError):
            slow_print_by_line("not a file")

    @patch('builtins.open', return_value=io.StringIO('Hello'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_slow_print_by_line(self, mock_output, _):
        slow_print_by_line('test_slow_rolling_text_printer.py')
        expected = 'Hello\n'
        self.assertEqual(mock_output.getvalue(), expected)
