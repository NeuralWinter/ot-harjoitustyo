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
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])


def roll_stats():
    return [roll_4d6_drop_lowest() for _ in range(6)]
