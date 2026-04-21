## Viikko 3

- Käyttäjä voi syöttää hahmon nimen
- Käyttäjä voi valita hahmon rodun (Human, Elf, Dwarf, Halfling)
- Käyttäjä voi valita hahmon luokan (Fighter, Wizard, Rogue, Cleric)
- Lisätty Character-luokka, joka vastaa hahmon tiedoista
- Lisätty Race-luokka, joka sisältää rotujen tiedot ja bonukset
- Lisätty CharacterClass-luokka, joka sisältää luokkien tiedot
- Lisätty CharacterCreation-luokka, joka vastaa käyttöliittymästä
- Testattu Character-luokan perustoiminnallisuus

## Viikko 4

- Lisätty stats-osio: käyttäjä voi valita standard array tai 4d6 drop lowest metodin
- Käyttäjä voi jakaa stat-arvot haluamiinsa ominaisuuksiin
- Rodun stat-bonukset lisätään automaattisesti hahmon statseihin
- Lisätty get_modifier-metodi joka laskee D&D:n mukaisen modifierin
- Lisätty Background-osio (Acolyte, Criminal, Soldier, Sage, Folk Hero)
- Lisätty Skills-järjestelmä, joka laskee taitoarvot statsien perusteella
- Luokan valinta rajoittaa nyt skill proficiency valintoja
- Background antaa automaattisesti 2 skill proficiencya
- Parannettu virheenkäsittelyä - virheelliset syötteet käsitellään nyt
- Lisätty testit Background ja Skills luokille
- Lisätty pylint koodin laadun tarkistukseen, koodi 10/10

## Viikko 5

- Lisätty graafinen käyttöliittymä tkinterilla
- Käyttäjä voi kulkea edestakaisin hahmonluontivaiheissa
- Lisätty nopanheitto statsien generointiin
- Yhteenvetonäkymä hahmon tiedoista
- Hahmo tallentuu JSON-tiedostoon