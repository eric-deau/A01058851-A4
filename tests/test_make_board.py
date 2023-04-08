from unittest import TestCase
from board.world_creation import make_board
from unittest.mock import patch


class TestMakeBoard(TestCase):
    @patch('random.randint', return_value=2)
    def test_make_board_min_size(self, _):
        expected_print = {(0, 0, 0): 'The air in the room is clear and warm. The room smells stale. '
                                     'A faint banging noise can be heard.',
                          (0, 1, 0): 'You feel an ominous presence coming from the door to the east..',
                          (1, 0, 0): 'You feel an ominous presence coming from the door to the south..',
                          (1, 1, 0): 'BOSS HERE'}
        self.assertEqual(expected_print, make_board(2, 2, 1))

    @patch('random.randint', return_value=2)
    def test_make_board_size_four_two_floors(self, _):
        expected_print = {(0, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 0, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 1, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 2, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 2, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 3, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 3, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 0, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 1, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 2, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 2, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 3, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 3, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 0, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 1, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 2, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 2, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (2, 3, 0): 'You feel an ominous presence coming from the door to the east..',
                          (2, 3, 1): 'You feel an ominous presence coming from the door to the east..',
                          (3, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (3, 0, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (3, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (3, 1, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (3, 2, 0): 'You feel an ominous presence coming from the door to the south..',
                          (3, 2, 1): 'You feel an ominous presence coming from the door to the south..',
                          (3, 3, 0): 'BOSS HERE',
                          (3, 3, 1): 'BOSS HERE'}
        self.assertEqual(expected_print, make_board(4, 4, 2))

    @patch('random.randint', return_value=2)
    def test_make_board_rectangle(self, _):
        expected_print = {(0, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (0, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                     'faint banging noise can be heard.',
                          (1, 1, 0): 'You feel an ominous presence coming from the door to the east..',
                          (2, 0, 0): 'You feel an ominous presence coming from the door to the south..',
                          (2, 1, 0): 'BOSS HERE'}
        self.assertEqual(expected_print, make_board(3, 2, 1))

    def test_make_board_incorrect_float_data_type(self):
        with self.assertRaises(TypeError):
            make_board(1.23, 32.1, 2.3)

    def test_make_board_incorrect_boolean_data_type(self):
        with self.assertRaises(TypeError):
            make_board(True, False, False)

    def test_make_board_incorrect_string_data_type(self):
        with self.assertRaises(TypeError):
            make_board("why are you", "doing this", "to me??")

    def test_make_board_incorrect_row_column_correct_floor(self):
        with self.assertRaises(ValueError):
            make_board(1, 1, 1)

    def test_make_board_all_incorrect(self):
        with self.assertRaises(ValueError):
            make_board(1, 1, 1)
