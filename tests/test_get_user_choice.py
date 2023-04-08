from unittest import TestCase
from unittest.mock import patch
from combat.game_combat import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value="2")
    def test_get_user_choice_in_options(self, _):
        expected = '2'
        self.assertEqual(expected, get_user_choice())

    @patch('builtins.input', return_value="NOT AN OPTION")
    def test_get_user_choice_not_in_options(self, _):
        expected = 'NOT AN OPTION'
        self.assertEqual(expected, get_user_choice())
