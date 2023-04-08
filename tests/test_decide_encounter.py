from unittest import TestCase
from unittest.mock import patch
from combat.encounters import decide_encounter
import io


class TestDecideEncounter(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_decide_encounter_false(self, _):
        expected = False
        self.assertEqual(expected, decide_encounter())

    @patch('random.randint', side_effect=[0])
    def test_decide_encounter_true(self, _):
        expected = True
        self.assertEqual(expected, decide_encounter())


