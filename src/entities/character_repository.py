"""Module for saving and loading characters to/from JSON files."""
import json
import os

class CharacterRepository:
    """Handles saving and loading characters to/from JSON files."""

    def __init__(self, directory="saved_characters"):
        """Initialize the repository with a save directory.

        Args:
            directory: Path to the directory where characters are saved
        """

        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save(self, character):
        """Save a character to a JSON file.

        Args:
            character: Character object to save

        Returns:
            The filename where the character was saved
        """

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
        """Load a character from a JSON file.

        Args:
            filename: Path to the JSON file

        Returns:
            Dictionary containing the character data
        """

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def list_characters(self):
        """List all saved character files.

        Returns:
            List of filenames in the save directory
        """

        files = os.listdir(self.directory)
        return [f for f in files if f.endswith(".json")]
