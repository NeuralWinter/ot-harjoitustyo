# Arkkitehtuuri

## Rakenne

Ohjelma on jaettu kolmeen pakkaukseen:

- **entities** - sovelluslogiikan luokat
- **tests** - yksikkötestit
- **ui** - käyttöliittymäkoodi

## Luokkakaavio
```mermaid
classDiagram
    CharacterCreation --> Character
    CharacterCreation --> RACES
    CharacterCreation --> CLASSES
    CharacterCreation --> BACKGROUNDS
    CharacterCreation --> SKILLS
    Character --> Race : race
    Character --> CharacterClass : character_class
    Character --> Background : background
    class Character{
        name
        race
        character_class
        level
        stats
        background
        skill_proficiencies
        set_stats()
        get_modifier()
        get_skill_value()
        add_skill_proficiency()
    }
    class Race{
        name
        stat_bonuses
        traits
    }
    class CharacterClass{
        name
        hit_die
        primary_stats
        traits
        allowed_skills
        skill_count
    }
    class Background{
        name
        skill_proficiencies
        description
    }
```