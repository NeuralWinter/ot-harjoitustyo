# Arkkitehtuuri

## Rakenne

Ohjelma on jaettu kolmeen pakkaukseen:

- **entities** - sovelluslogiikan luokat
- **tests** - yksikkötestit
- **ui** - käyttöliittymäkoodi

## Sovelluslogiikka

Sovelluksen sovelluslogiikka on jaettu `entities`-pakkaukseen, joka sisältää seuraavat luokat:

- **Character** – vastaa hahmon tiedoista ja laskuista. Sisältää metodit statsien asettamiseen, ability modifier laskentaan ja skill proficiencyjen hallintaan.
- **Race** – sisältää rodun tiedot ja stat-bonukset. Bonukset lisätään automaattisesti hahmon statseihin rodun valinnan yhteydessä.
- **CharacterClass** – sisältää luokan tiedot, sallitut skillsit ja skill valintojen määrän.
- **Background** – sisältää taustan tiedot ja automaattisesti annettavat skill proficiencyt.
- **CharacterRepository** – vastaa hahmojen tallennuksesta ja lataamisesta JSON-tiedostoihin.
- **PDFGenerator** – vastaa hahmon character sheetin generoinnista PDF-muotoon reportlab-kirjaston avulla.

Käyttöliittymä on eriytetty `ui`-pakkaukseen, joka sisältää:

- **CharacterCreatorGUI** – graafinen tkinter-käyttöliittymä hahmon luontiin, lataamiseen ja PDF-exporttiin.

## Tietojen pysyväistallennus

Hahmot tallennetaan JSON-tiedostoihin `saved_characters`-hakemistoon. Jokainen hahmo tallennetaan omaan tiedostoonsa, jonka nimi muodostuu hahmon nimestä. JSON-tiedosto sisältää hahmon kaikki tiedot: nimen, rodun, luokan, taustan, statsit ja skill proficiencyt.

PDF-tiedostot generoidaan samaan `saved_characters`-hakemistoon reportlab-kirjaston avulla.

## Luokkakaavio

```mermaid
classDiagram
    CharacterCreatorGUI --> Character
    CharacterCreatorGUI --> RACES
    CharacterCreatorGUI --> CLASSES
    CharacterCreatorGUI --> BACKGROUNDS
    CharacterCreatorGUI --> SKILLS
    CharacterCreatorGUI --> CharacterRepository
    CharacterCreatorGUI --> PDFGenerator
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
    class CharacterRepository{
        save()
        load()
        list_characters()
    }
    class PDFGenerator{
        generate()
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