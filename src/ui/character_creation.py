from entities.race import RACES
from entities.character_class import CLASSES
from entities.character import Character
from entities.stats import STANDARD_ARRAY, STAT_NAMES, roll_stats
from entities.background import BACKGROUNDS
from entities.skills import SKILLS


class CharacterCreation:
    def create_character(self):
        print("\n*** D&D 5e Character Creator ***\n")

        name = input("Enter your character's name: ")
        race = self._choose_race()
        character_class = self._choose_class()
        background = self._choose_background()
        stats = self._choose_stats()

        character = Character(name)
        character.race = race.name
        character.character_class = character_class.name
        character.background = background.name
        character.set_stats(stats, race)

        for skill in background.skill_proficiencies:
            character.add_skill_proficiency(skill)

        self._choose_class_skills(character, character_class)
        self._print_character(character)

        return character

    def _get_valid_number(self, prompt, min_val, max_val):
        while True:
            try:
                choice = int(input(prompt))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Please enter a valid number.")

    def _choose_race(self):
        print("\nChoose your race:")
        races = list(RACES.values())
        for i, race in enumerate(races, 1):
            print(f"{i}. {race.name}")
        choice = self._get_valid_number("Enter number: ", 1, len(races))
        return races[choice - 1]

    def _choose_class(self):
        print("\nChoose your class:")
        classes = list(CLASSES.values())
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls.name}")
        choice = self._get_valid_number("Enter number: ", 1, len(classes))
        return classes[choice - 1]

    def _choose_background(self):
        print("\nChoose your background:")
        backgrounds = list(BACKGROUNDS.values())
        for i, bg in enumerate(backgrounds, 1):
            print(f"{i}. {bg.name} - {bg.description}")
        choice = self._get_valid_number("Enter number: ", 1, len(backgrounds))
        selected = backgrounds[choice - 1]
        print(f"\nBackground skills: {', '.join(selected.skill_proficiencies)}")
        return selected

    def _choose_stats(self):
        print("\nChoose stat method:")
        print("1. Standard Array [15, 14, 13, 12, 10, 8]")
        print("2. Roll 4d6 drop lowest")
        choice = self._get_valid_number("Enter number: ", 1, 2)

        if choice == 1:
            values = STANDARD_ARRAY.copy()
        else:
            values = roll_stats()
            print(f"\nYou rolled: {sorted(values, reverse=True)}")

        stats = {}
        available = sorted(values, reverse=True)
        print("\nAssign your stats (highest to lowest):")
        for value in available:
            print(f"\nAssign {value} to which stat?")
            remaining = [s for s in STAT_NAMES if s not in stats]
            for i, stat in enumerate(remaining, 1):
                print(f"{i}. {stat.capitalize()}")
            stat_choice = self._get_valid_number("Enter number: ", 1, len(remaining))
            stats[remaining[stat_choice - 1]] = value

        return stats

    def _choose_class_skills(self, character, character_class):
        available_skills = [
            s for s in SKILLS if s not in character.skill_proficiencies
        ]
        print("\nChoose 2 skill proficiencies for your class:")
        for i, skill in enumerate(available_skills, 1):
            print(f"{i}. {skill.replace('_', ' ').capitalize()}")

        for _ in range(2):
            choice = self._get_valid_number("Enter number: ", 1, len(available_skills))
            skill = available_skills[choice - 1]
            character.add_skill_proficiency(skill)
            available_skills.remove(skill)
            print(f"Added: {skill.replace('_', ' ').capitalize()}")

    def _print_character(self, character):
        print(f"\n{'='*40}")
        print(f"Character: {character}")
        print(f"Background: {character.background}")
        stat_order = ["strength", "dexterity", "constitution", "wisdom", "intelligence", "charisma"]
        print(f"\nStats:")
        for stat in stat_order:
            value = character.stats[stat]
            modifier = character.get_modifier(stat)
            sign = "+" if modifier >= 0 else ""
            print(f"  {stat.capitalize()}: {value} ({sign}{modifier})")
        print(f"\nSkill Proficiencies:")
        for skill in sorted(character.skill_proficiencies):
            value = character.get_skill_value(skill)
            sign = "+" if value >= 0 else ""
            print(f"  {skill.replace('_', ' ').capitalize()}: {sign}{value}")
