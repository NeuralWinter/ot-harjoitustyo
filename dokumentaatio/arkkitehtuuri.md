# Arkkitehtuuri

## Rakenne

Ohjelma on jaettu kolmeen pakkaukseen:

- **entities** - sovelluslogiikan luokat
- **tests** - yksikkötestit
- **ui** - käyttöliittymäkoodi

## Sovelluslogiikka

Sovelluksen sovelluslogiikka on jaettu `entities`-pakkaukseen, joka sisältää seuraavat luokat:

- **Character** – vastaa hahmon tiedoista ja laskuista
- **Race** – sisältää rodun tiedot ja stat-bonukset
- **CharacterClass** – sisältää luokan tiedot ja sallitut skillsit
- **Background** – sisältää taustan tiedot ja skill proficiencyt
- **CharacterRepository** – vastaa hahmojen tallennuksesta ja lataamisesta JSON-tiedostoihin

Käyttöliittymä on eriytetty `ui`-pakkaukseen, joka sisältää:

- **CharacterCreatorGUI** – graafinen tkinter-käyttöliittymä
- **CharacterCreation** – tekstipohjainen käyttöliittymä (kehityskäyttöön)

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
## Sekvenssikaavio: Hahmon luonti ja tallennus

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant GUI as CharacterCreatorGUI
    participant Character
    participant RACES
    participant CharacterRepository

    Käyttäjä->>GUI: Syöttää nimen, rodun, luokan, taustan, statsit ja skillsit
    GUI->>RACES: Hakee valitun rodun tiedot
    RACES-->>GUI: Race-olio
    GUI->>Character: Character(nimi)
    GUI->>Character: set_stats(statsit, rotu)
    Character-->>GUI: Statsit rodun bonuksineen
    GUI->>Character: add_skill_proficiency(skill)
    Käyttäjä->>GUI: Painaa "Save Character"
    GUI->>CharacterRepository: save(character)
    CharacterRepository-->>GUI: filename
    GUI-->>Käyttäjä: "Character Saved!"
```