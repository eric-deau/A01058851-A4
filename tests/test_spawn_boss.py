from unittest import TestCase
from unittest.mock import patch
from combat.encounters import spawn_boss
import io


class TestSpawnBoss(TestCase):
    @patch('builtins.open', return_value=io.StringIO('[{"Name": "EYE OF CTHULHU", "HP": 30, "ATK": 25,'
                                                     ' "Affliction": null, "Turn": false, "EXP": 100}]'))
    def test_spawn_boss_floor_one(self, _):
        test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 4,
                         'Y-coord': 4, 'Z-coord': 0, 'HP': 300, 'MP': 200, 'EXP': 50, 'Level': 1, 'Turn': False,
                         'Affliction': None}
        test_file_content = spawn_boss(test_char_one)
        expected = {"Name": "EYE OF CTHULHU", "HP": 30, "ATK": 25, "Affliction": None, "Turn": False, "EXP": 100}
        self.assertEqual(expected, test_file_content)

    class TestSpawnBoss(TestCase):
        @patch('builtins.open', return_value=io.StringIO('[{"Name": "EYE OF CTHULHU", "HP": 30, "ATK": 25,'
                                                         ' "Affliction": null, "Turn": false, "EXP": 100},'
                                                         ' {"Name": "Banana", "HP": 30, "ATK": 25,'
                                                         ' "Affliction": null, "Turn": false, "EXP": 100}]'))
        def test_spawn_boss_floor_two(self, _):
            test_char_one = {'Name': 'RAKSHASA', 'Class': 'Mage', 'Attack': 70, 'Spell': 'Doomsday', 'X-coord': 4,
                             'Y-coord': 4, 'Z-coord': 1, 'HP': 300, 'MP': 200, 'EXP': 50, 'Level': 1, 'Turn': False,
                             'Affliction': None}
            test_file_content = spawn_boss(test_char_one)
            expected = {"Name": "Banana", "HP": 40, "ATK": 25, "Affliction": None, "Turn": False, "EXP": 100}
            self.assertEqual(expected, test_file_content)
