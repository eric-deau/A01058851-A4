from unittest import TestCase
from unittest.mock import patch
from board.world_creation import add_bosses


class TestAddBosses(TestCase):
    def test_add_bosses_min_size(self):
        test_board = {(0, 0, 0): 'The air in the room is clear and warm. The room smells stale. '
                                 'A faint banging noise can be heard.',
                      (0, 1, 0): 'something something.',
                      (1, 0, 0): 'I don\'t know what to put here',
                      (1, 1, 0): 'BOSS HERE'}
        add_bosses(test_board, 2, 2, 1)
        expected = {(0, 0, 0): 'The air in the room is clear and warm. The room smells stale. '
                               'A faint banging noise can be heard.',
                    (0, 1, 0): 'You feel an ominous presence coming from the door to the east..',
                    (1, 0, 0): 'You feel an ominous presence coming from the door to the south..',
                    (1, 1, 0): 'BOSS HERE'}
        self.assertEqual(expected, test_board)

    def test_add_bosses_four_row_four_col_two_floor(self):
        test_board = {(0, 0, 0): 'Really really really really long text.',
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
                      (1, 3, 0): 'Hiding some text here blah blah blah hi tester',
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
                      (2, 3, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (2, 3, 1): 'Just saying but if you play my game, pick warrior. I made that class super OP.',
                      (3, 0, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 0, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 1, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 1, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 2, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 2, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 3, 0): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.',
                      (3, 3, 1): 'The air in the room is clear and warm. The room smells stale. A '
                                 'faint banging noise can be heard.'}
        add_bosses(test_board, 4, 4, 2)
        expected = {(0, 0, 0): 'Really really really really long text.',
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
                    (1, 3, 0): 'Hiding some text here blah blah blah hi tester',
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
        self.assertEqual(expected, test_board)

    def test_add_bosses_incorrect_board_type(self):
        with self.assertRaises(TypeError):
            add_bosses("not a board", 3, 3, 3)

    def test_add_bosses_correct_board_incorrect_rows_cols_floors(self):
        with self.assertRaises(TypeError):
            add_bosses({"pretend this is a board": "but it isn't"}, 3.1, 3.2, 3.3)

    def test_add_bosses_incorrect_values(self):
        with self.assertRaises(ValueError):
            add_bosses({"pretend this is a board": "but it isn't"}, 1, 1, 2)

    def test_add_bosses_nonexistent_coordinates(self):
        with self.assertRaises(KeyError):
            add_bosses({"pretend this is a board": "but it isn't"}, 3, 3, 2)




