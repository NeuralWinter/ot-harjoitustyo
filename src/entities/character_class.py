class CharacterClass:
    def __init__(self, name, hit_die, primary_stats, traits):
        self.name = name
        self.hit_die = hit_die
        self.primary_stats = primary_stats
        self.traits = traits

    def __str__(self):
        return self.name


CLASSES = {
    "Fighter": CharacterClass(
        "Fighter",
        10,
        ["strength", "constitution"],
        ["Fighting Style", "Second Wind"]
    ),
    "Wizard": CharacterClass(
        "Wizard",
        6,
        ["intelligence", "wisdom"],
        ["Arcane Recovery", "Spellcasting"]
    ),
    "Rogue": CharacterClass(
        "Rogue",
        8,
        ["dexterity", "intelligence"],
        ["Expertise", "Sneak Attack", "Thieves' Cant"]
    ),
    "Cleric": CharacterClass(
        "Cleric",
        8,
        ["wisdom", "charisma"],
        ["Divine Domain", "Spellcasting"]
    )
}