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

    def set_stats(self, stats, race=None):
        self.stats = stats
        if race and race.stat_bonuses:
            for stat, bonus in race.stat_bonuses.items():
                if stat in self.stats:
                    self.stats[stat] += bonus

    def get_modifier(self, stat):
        return (self.stats[stat] - 10) // 2

    def __str__(self):
        return (
            f"{self.name} - Race: {self.race}, "
            f"Class: {self.character_class}, Level: {self.level}"
        )
