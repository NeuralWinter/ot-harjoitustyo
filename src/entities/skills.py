SKILLS = {
    "acrobatics": "dexterity",
    "animal_handling": "wisdom",
    "arcana": "intelligence",
    "athletics": "strength",
    "deception": "charisma",
    "history": "intelligence",
    "insight": "wisdom",
    "intimidation": "charisma",
    "investigation": "intelligence",
    "medicine": "wisdom",
    "nature": "intelligence",
    "perception": "wisdom",
    "performance": "charisma",
    "persuasion": "charisma",
    "religion": "intelligence",
    "sleight_of_hand": "dexterity",
    "stealth": "dexterity",
    "survival": "wisdom"
}

PROFICIENCY_BONUS = 2


def calculate_skill_value(skill, stats, proficiencies):
    stat = SKILLS[skill]
    modifier = (stats[stat] - 10) // 2
    if skill in proficiencies:
        return modifier + PROFICIENCY_BONUS
    return modifier
