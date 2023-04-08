from unittest import TestCase
from unittest.mock import patch
from character.character_creation import choose_name


class TestChooseName(TestCase):
    @patch('builtins.input', side_effect=["Bobby B", "Y"])
    def test_choose_name_correct_inputs(self, _):
        actual = choose_name()
        expected = "Bobby B"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Bobby B", "NO NOT THIS NAME", "Bobby but with a B", "Y"])
    def test_choose_name_rechoose_name(self, _):
        actual = choose_name()
        expected = "Bobby but with a B"
        self.assertEqual(expected, actual)
