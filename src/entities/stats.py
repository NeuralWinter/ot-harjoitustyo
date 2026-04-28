"""Module containing stat generation functions for D&D 5e characters."""
import random

STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

STAT_NAMES = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
]


def roll_4d6_drop_lowest():
    """Roll 4d6 and drop the lowest die, returning the sum.

    Returns:
        Integer between 3 and 18
    """

    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])


def roll_stats():
    """Generate a full set of 6 ability scores using 4d6 drop lowest method.

    Returns:
        List of 6 integers
    """

    return [roll_4d6_drop_lowest() for _ in range(6)]
