import unittest
from entities.character import Character
from entities.race import RACES


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

    def test_set_stats_assigns_correctly(self):
        stats = {
            "strength": 15, "dexterity": 14, "constitution": 13,
            "intelligence": 12, "wisdom": 10, "charisma": 8
        }
        self.character.set_stats(stats)
        self.assertEqual(self.character.stats["strength"], 15)

    def test_race_bonuses_applied_to_stats(self):
        stats = {
            "strength": 15, "dexterity": 14, "constitution": 13,
            "intelligence": 12, "wisdom": 10, "charisma": 8
        }
        human = RACES["Human"]
        self.character.set_stats(stats, human)
        self.assertEqual(self.character.stats["strength"], 16)

    def test_get_modifier_positive(self):
        self.character.stats["strength"] = 16
        self.assertEqual(self.character.get_modifier("strength"), 3)

    def test_get_modifier_negative(self):
        self.character.stats["charisma"] = 8
        self.assertEqual(self.character.get_modifier("charisma"), -1)
