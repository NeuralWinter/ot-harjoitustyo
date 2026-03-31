from entities.race import RACES
from entities.character_class import CLASSES
from entities.character import Character


class CharacterCreation:
    def create_character(self):
        print("\n*** D&D 5e Character Creator ***\n")

        name = input("Enter your character's name: ")

        race = self._choose_race()
        character_class = self._choose_class()

        character = Character(name)
        character.race = race.name
        character.character_class = character_class.name

        print(f"\nCharacter created: {character}")
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