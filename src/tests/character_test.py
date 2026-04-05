import unittest
from entities.character import Character
from entities.race import RACES
from entities.background import BACKGROUNDS
from entities.skills import calculate_skill_value
from entities.stats import roll_4d6_drop_lowest
from entities.character_class import CLASSES

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

class TestBackground(unittest.TestCase):
    def test_background_has_correct_skills(self):
        criminal = BACKGROUNDS["Criminal"]
        self.assertIn("deception", criminal.skill_proficiencies)
        self.assertIn("stealth", criminal.skill_proficiencies)

class TestSkills(unittest.TestCase):
    def test_skill_value_without_proficiency(self):
        stats = {"dexterity": 14, "strength": 10, "constitution": 10,
                 "intelligence": 10, "wisdom": 10, "charisma": 10}
        value = calculate_skill_value("acrobatics", stats, [])
        self.assertEqual(value, 2)

    def test_skill_value_with_proficiency(self):
        stats = {"dexterity": 14, "strength": 10, "constitution": 10,
                 "intelligence": 10, "wisdom": 10, "charisma": 10}
        value = calculate_skill_value("acrobatics", stats, ["acrobatics"])
        self.assertEqual(value, 4)

class TestStats(unittest.TestCase):
    def test_roll_4d6_drop_lowest_range(self):
        for _ in range(1000):
            result = roll_4d6_drop_lowest()
            self.assertTrue(3 <= result <= 18)

class TestCharacterClass(unittest.TestCase):
    def test_fighter_has_correct_skill_count(self):
        fighter = CLASSES["Fighter"]
        self.assertEqual(fighter.skill_count, 2)

    def test_wizard_allowed_skills_contains_arcana(self):
        wizard = CLASSES["Wizard"]
        self.assertIn("arcana", wizard.allowed_skills)

    def test_rogue_has_four_skill_choices(self):
        rogue = CLASSES["Rogue"]
        self.assertEqual(rogue.skill_count, 4)
