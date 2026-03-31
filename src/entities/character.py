class Character:
    def __init__(self, name):
        self.name = name
        self.race = None
        self.character_class = None
        self.level = 1
        self.stats = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

    def __str__(self):
        return f"{self.name} - Race: {self.race}, Class: {self.character_class}, Level: {self.level}"