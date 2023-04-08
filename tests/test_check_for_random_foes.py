from unittest import TestCase
from unittest.mock import patch
from utilities.game_checks import check_for_random_foes


class TestCheckForRandomFoes(TestCase):
    @patch('random.randint', side_effect=[2])
    def test_check_for_random_foes_no_foe(self, _):
        actual_one = check_for_random_foes()
        self.assertEqual(False, actual_one)

    @patch('random.randint', side_effect=[1])
    def test_check_for_random_foes_is_foe(self, _):
        actual_two = check_for_random_foes()
        self.assertEqual(True, actual_two)
