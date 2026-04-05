from entities.race import RACES
from entities.character_class import CLASSES
from entities.character import Character
from entities.stats import STANDARD_ARRAY, STAT_NAMES, roll_stats


class CharacterCreation:
    def create_character(self):
        print("\n*** D&D 5e Character Creator ***\n")

        name = input("Enter your character's name: ")
        race = self._choose_race()
        character_class = self._choose_class()
        stats = self._choose_stats()

        character = Character(name)
        character.race = race.name
        character.character_class = character_class.name
        character.set_stats(stats, race)

        print(f"\nCharacter created: {character}")
        print("\nStats:")
        for stat, value in character.stats.items():
            modifier = character.get_modifier(stat)
            sign = "+" if modifier >= 0 else ""
            print(f"  {stat.capitalize()}: {value} ({sign}{modifier})")
        
        return character

    def _choose_race(self):
        print("\nChoose your race:")
        races = list(RACES.values())
        for i, race in enumerate(races, 1):
            print(f"{i}. {race.name}")
        choice = int(input("Enter number: ")) - 1
        return races[choice]

    def _choose_class(self):
        print("\nChoose your class:")
        classes = list(CLASSES.values())
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls.name}")
        choice = int(input("Enter number: ")) - 1
        return classes[choice]
    
    def _choose_stats(self):
        print("\nChoose stat method:")
        print("1. Standard Array [15, 14, 13, 12, 10, 8]")
        print("2. Roll 4d6 drop lowest")
        choice = input("Enter number: ")

        if choice == "1":
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
            stat_choice = int(input("Enter number: ")) - 1
            stats[remaining[stat_choice]] = value

        return stats
   