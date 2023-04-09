from unittest import TestCase
from unittest.mock import patch
from board.lore import beginning_of_game
import io


class TestBeginningOfGame(TestCase):

    def test_beginning_of_game_file_non_existent(self):
        with self.assertRaises(FileNotFoundError):
            beginning_of_game()

    @patch('builtins.open', return_value=io.StringIO('Hello'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_beginning_of_game(self, mock_output, _):
        beginning_of_game()
        expected = 'Hello\n'
        self.assertEqual(mock_output.getvalue(), expected)
