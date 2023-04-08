from unittest import TestCase
from utilities.game_checks import check_for_boss


class TestCheckForBoss(TestCase):
    def test_check_for_boss_true(self):
        test_board = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Test', (0, 0, 2): 'Test',
                      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test',
                      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test',
                      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test',
                      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test',
                      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test',
                      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test',
                      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test',
                      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test',
                      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test',
                      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test',
                      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test',
                      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test',
                      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test',
                      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test',
                      (4, 4, 0): 'BOSS HERE', (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
        test_char = {'X-coord': 4, 'Y-coord': 4, 'Z-coord': 0, 'HP': 2}
        expected = True
        self.assertEqual(expected, check_for_boss(current_char=test_char, current_board=test_board))

    def test_check_for_boss_false(self):
        test_board = {(0, 0, 0): ':D', (0, 0, 1): 'Test', (0, 0, 2): 'Test',
                      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test',
                      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test',
                      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test',
                      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test',
                      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test',
                      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test',
                      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test',
                      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test',
                      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test',
                      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test',
                      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test',
                      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test',
                      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test',
                      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test',
                      (4, 4, 0): 'BOSS HERE', (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
        test_char = {'X-coord': 3, 'Y-coord': 4, 'Z-coord': 0, 'HP': 2}
        expected = False
        self.assertEqual(expected, check_for_boss(current_char=test_char, current_board=test_board))

    def test_check_for_boss_true_different_z_coord(self):
        test_board = {(0, 0, 0): ':)', (0, 0, 1): 'Test', (0, 0, 2): 'Test',
                      (0, 1, 0): 'Test', (0, 1, 1): 'Test', (0, 1, 2): 'Test', (0, 2, 0): 'Test', (0, 2, 1): 'Test',
                      (0, 2, 2): 'Test', (0, 3, 0): 'Test', (0, 3, 1): 'Test', (0, 3, 2): 'Test', (0, 4, 0): 'Test',
                      (0, 4, 1): 'Test', (0, 4, 2): 'Test', (1, 0, 0): 'Test', (1, 0, 1): 'Test', (1, 0, 2): 'Test',
                      (1, 1, 0): 'Test', (1, 1, 1): 'Test', (1, 1, 2): 'Test', (1, 2, 0): 'Test', (1, 2, 1): 'Test',
                      (1, 2, 2): 'Test', (1, 3, 0): 'Test', (1, 3, 1): 'Test', (1, 3, 2): 'Test', (1, 4, 0): 'Test',
                      (1, 4, 1): 'Test', (1, 4, 2): 'Test', (2, 0, 0): 'Test', (2, 0, 1): 'Test', (2, 0, 2): 'Test',
                      (2, 1, 0): 'Test', (2, 1, 1): 'Test', (2, 1, 2): 'Test', (2, 2, 0): 'Test', (2, 2, 1): 'Test',
                      (2, 2, 2): 'Test', (2, 3, 0): 'Test', (2, 3, 1): 'Test', (2, 3, 2): 'Test', (2, 4, 0): 'Test',
                      (2, 4, 1): 'Test', (2, 4, 2): 'Test', (3, 0, 0): 'Test', (3, 0, 1): 'Test', (3, 0, 2): 'Test',
                      (3, 1, 0): 'Test', (3, 1, 1): 'Test', (3, 1, 2): 'Test', (3, 2, 0): 'Test', (3, 2, 1): 'Test',
                      (3, 2, 2): 'Test', (3, 3, 0): 'Test', (3, 3, 1): 'Test', (3, 3, 2): 'Test', (3, 4, 0): 'Test',
                      (3, 4, 1): 'Test', (3, 4, 2): 'Test', (4, 0, 0): 'Test', (4, 0, 1): 'Test', (4, 0, 2): 'Test',
                      (4, 1, 0): 'Test', (4, 1, 1): 'Test', (4, 1, 2): 'Test', (4, 2, 0): 'Test', (4, 2, 1): 'Test',
                      (4, 2, 2): 'Test', (4, 3, 0): 'Test', (4, 3, 1): 'Test', (4, 3, 2): 'Test',
                      (4, 4, 0): 'BOSS HERE', (4, 4, 1): 'BOSS HERE', (4, 4, 2): 'BOSS HERE'}
        test_char = {'X-coord': 4, 'Y-coord': 4, 'Z-coord': 2, 'HP': 2}
        expected = True
        self.assertEqual(expected, check_for_boss(current_char=test_char, current_board=test_board))

    def test_check_for_boss_true_small_board(self):
        test_board = {(0, 0, 0): 'Looks like this is my starting point.', (0, 0, 1): 'Description One',
                      (0, 1, 0): 'Description Two', (0, 1, 1): 'Description Three', (1, 0, 0): 'Description Four',
                      (1, 0, 1): 'Description Five', (1, 1, 0): 'BOSS HERE', (1, 1, 1): 'BOSS HERE'}
        test_char = {'X-coord': 1, 'Y-coord': 1, 'Z-coord': 0, 'HP': 2}
        expected = True
        self.assertEqual(expected, check_for_boss(current_char=test_char, current_board=test_board))
