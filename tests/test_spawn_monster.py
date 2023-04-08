import io
from unittest import TestCase
from unittest.mock import patch
from combat.encounters import spawn_monster


class TestSpawnMonster(TestCase):

    @patch('builtins.open', return_value=io.StringIO('[{"Name": "EYE OF CTHULHU", "HP": 30, "ATK": 25,'
                                                     ' "Affliction": null, "Turn": false, "EXP": 100}]'))
    @patch('random.randint', side_effect=[0, 50])
    def test_spawn_monster_length_of_one(self, _, __):
        test_file_content = spawn_monster()
        expected = {"Name": "EYE OF CTHULHU", "HP": 50, "ATK": 25, "Affliction": None, "Turn": False, "EXP": 100}
        self.assertEqual(expected, test_file_content)

    @patch('builtins.open', return_value=io.StringIO('[{"Name": "EYE OF CTHULHU", "HP": 30, "ATK": 25,'
                                                     ' "Affliction": null, "Turn": false, "EXP": 100},'
                                                     ' {"Name": "Banana", "HP": 30, "ATK": 25,'
                                                     ' "Affliction": null, "Turn": false, "EXP": 100}]'))
    @patch('random.randint', side_effect=[1, 40])
    def test_spawn_monster_length_of_two(self, _, __):
        test_file_content = spawn_monster()
        expected = {"Name": "Banana", "HP": 40, "ATK": 25, "Affliction": None, "Turn": False, "EXP": 100}
        self.assertEqual(expected, test_file_content)
