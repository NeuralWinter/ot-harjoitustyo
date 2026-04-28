class Race:
    """Represents a D&D 5e playable race."""

    def __init__(self, name, stat_bonuses, traits):
        """Initialize a race with its properties.
        
        Aargs:
            name: The race name
            stat_bonuses: Dictionary of ability score bonuses
            traits: List of racial trait names
        """

        self.name = name
        self.stat_bonuses = stat_bonuses
        self.traits = traits


    def __str__(self):
        return self.name


RACES = {
    "Human": Race(
        "Human",
        {"strength": 1, "dexterity": 1, "constitution": 1,
         "intelligence": 1, "wisdom": 1, "charisma": 1},
        ["Extra Language", "Extra Skill"]
    ),
    "Elf": Race(
        "Elf",
        {"dexterity": 2, "intelligence": 1},
        ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"]
    ),
    "Dwarf": Race(
        "Dwarf",
        {"constitution": 2, "wisdom": 1},
        ["Darkvision", "Dwarven Resilience", "Stonecunning"]
    ),
    "Halfling": Race(
        "Halfling",
        {"dexterity": 2, "charisma": 1},
        ["Lucky", "Brave", "Halfling Nimbleness"]
    )
}
