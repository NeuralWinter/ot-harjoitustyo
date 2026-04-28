class Background:
    """Represents a D&D 5e character background."""

    def __init__(self, name, skill_proficiencies, description):
        """Initialize a background with its properties.

        Args:
            name: The background name
            skill_proficiencies: List of skills granted by this background
            description: Short description of the background
        """

        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.description = description

    def __str__(self):
        return self.name


BACKGROUNDS = {
    "Acolyte": Background(
        "Acolyte",
        ["insight", "religion"],
        "You have spent your life in service to a temple."
    ),
    "Criminal": Background(
        "Criminal",
        ["deception", "stealth"],
        "You have a history of breaking the law."
    ),
    "Soldier": Background(
        "Soldier",
        ["athletics", "intimidation"],
        "You have fought in wars and know the horrors of battle."
    ),
    "Sage": Background(
        "Sage",
        ["arcana", "history"],
        "You spent years learning the lore of the multiverse."
    ),
    "Folk Hero": Background(
        "Folk Hero",
        ["animal_handling", "survival"],
        "You come from a humble background but are destined for greatness."
    )
}
