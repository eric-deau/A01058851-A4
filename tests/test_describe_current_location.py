import io
from unittest import TestCase
from unittest.mock import patch
from movement.movement import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_starting_point(self, mock_output):
        char_one = {'X-coord': 0, 'Y-coord': 0, 'Z-coord': 0, "HP": 2}
        board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One',
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        describe_current_location(current_char=char_one, board=board_one)
        expected = 'Looks like this is my starting point.\nYou are currently in: Hell\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_last_x_y_coordinate(self, mock_output):
        char_one = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 0, "HP": 2}
        board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One',
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        describe_current_location(current_char=char_one, board=board_one)
        expected = 'Description Six\nYou are currently in: Hell\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_different_floor(self, mock_output):
        char_one = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 1, "HP": 2}
        board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One',
                     (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                     (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
        describe_current_location(current_char=char_one, board=board_one)
        expected = 'Description Seven\nYou are currently in: Earth\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_describe_current_location_incorrect_coordinates(self):
        with self.assertRaises(KeyError):
            char_one = {'X-coord': -1, 'Y-coord': 1, 'Z-coord': 0, "HP": 2}
            board_one = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One',
                         (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                         (1, 0, 1): 'Description Five', (1, 1, 0): 'Description Six', (1, 1, 1): 'Description Seven'}
            describe_current_location(current_char=char_one, board=board_one)
