from unittest import TestCase
from character.character_creation import get_skill


class TestGetSkill(TestCase):
    def test_get_skill_warrior(self):
        actual = get_skill("Warrior")
        expected = "Earthquake Chain"
        self.assertEqual(expected, actual)

    def test_get_skill_mage(self):
        actual = get_skill("Mage")
        expected = "Doomsday"
        self.assertEqual(expected, actual)

    def test_get_skill_thief(self):
        actual = get_skill("Thief")
        expected = "Stab"
        self.assertEqual(expected, actual)

    def test_get_skill_incorrect_data_type(self):
        with self.assertRaises(TypeError):
            get_skill(43110)

    def test_get_skill_incorrect_value(self):
        with self.assertRaises(ValueError):
            get_skill("Rogue")


