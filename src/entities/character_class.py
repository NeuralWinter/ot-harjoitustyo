class CharacterClass:
    def __init__(self, name, traits, skill_config, class_config):
        self.name = name
        self.hit_die = class_config["hit_die"]
        self.primary_stats = class_config["primary_stats"]
        self.traits = traits
        self.allowed_skills = skill_config["allowed_skills"]
        self.skill_count = skill_config["skill_count"]

    def __str__(self):
        return self.name

CLASSES = {
    "Fighter": CharacterClass(
        "Fighter",
        ["Fighting Style", "Second Wind"],
        {
            "allowed_skills": ["acrobatics", "animal_handling", "athletics",
                            "history", "insight", "intimidation",
                            "perception", "survival"],
            "skill_count": 2
        },
        {
            "hit_die": 10,
            "primary_stats": ["strength", "constitution"]
        }
    ),
    "Wizard": CharacterClass(
        "Wizard",
        ["Arcane Recovery", "Spellcasting"],
        {
            "allowed_skills": ["arcana", "history", "insight",
                            "investigation", "medicine", "religion"],
            "skill_count": 2
        },
        {
            "hit_die": 6,
            "primary_stats": ["intelligence", "wisdom"]
        }
    ),
    "Rogue": CharacterClass(
        "Rogue",
        ["Expertise", "Sneak Attack", "Thieves Cant"],
        {
            "allowed_skills": ["acrobatics", "athletics", "deception",
                            "insight", "intimidation", "investigation",
                            "perception", "performance", "persuasion",
                            "sleight_of_hand", "stealth"],
            "skill_count": 4
        },
        {
            "hit_die": 8,
            "primary_stats": ["dexterity", "intelligence"]
        }
    ),
    "Cleric": CharacterClass(
        "Cleric",
        ["Spellcasting", "Divine Domain"],
        {
            "allowed_skills": ["history", "insight", "medicine",
                            "persuasion", "religion"],
            "skill_count": 2
        },
        {
            "hit_die": 8,
            "primary_stats": ["wisdom", "charisma"]
        }
    )
}
