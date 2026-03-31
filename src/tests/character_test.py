import unittest
from entities.character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Bob")

    def test_character_name_is_set_correctly(self):
        self.assertEqual(self.character.name, "Bob")

    def test_character_initial_level_is_one(self):
        self.assertEqual(self.character.level, 1)

    def test_character_race_can_be_set(self):
        self.character.race = "Halfling"
        self.assertEqual(self.character.race, "Halfling")

    def test_character_class_can_be_set(self):
        self.character.character_class = "Rogue"
        self.assertEqual(self.character.character_class, "Rogue")