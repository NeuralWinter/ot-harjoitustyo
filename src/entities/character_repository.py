import json
import os


class CharacterRepository:
    def __init__(self, directory="saved_characters"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save(self, character):
        data = {
            "name": character.name,
            "race": character.race,
            "character_class": character.character_class,
            "level": character.level,
            "background": character.background,
            "stats": character.stats,
            "skill_proficiencies": character.skill_proficiencies
        }
        filename = f"{self.directory}/{character.name.lower().replace(' ', '_')}.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        return filename

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def list_characters(self):
        files = os.listdir(self.directory)
        return [f for f in files if f.endswith(".json")]
