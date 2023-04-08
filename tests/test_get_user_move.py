from unittest import TestCase
from unittest.mock import patch
from movement.movement import get_user_move


class TestGetUserMove(TestCase):
    @patch('builtins.input', side_effect=['fdsafdsa', '1'])
    def test_get_user_move_wrong_input_once(self, _):
        actual = get_user_move()
        expected = 'North Door'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_move_once(self, _):
        actual = get_user_move()
        expected = 'West Door'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['554', 'dasfd', '421', '2'])
    def test_get_user_move_wrong_input_multiple_times(self, _):
        actual = get_user_move()
        expected = 'South Door'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_move_lower_bound(self, _):
        actual = get_user_move()
        expected = 'North Door'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_move_upper_bound(self, _):
        actual = get_user_move()
        expected = 'East Door'
        self.assertEqual(expected, actual)
