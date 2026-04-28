## Dungeons & Dragons 5e -hahmonluontityökalu

Sovellus on **Dungeons & Dragons 5e** -hahmonluontityökalu, joka opastaa käyttäjää *askel askeleelta* hahmon luonnissa vaihtoehtojen joukosta ja tulostaa lopuksi valmiin character sheetin PDF-muodossa.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Release](https://github.com/NeuralWinter/ot-harjoitustyo/releases/tag/viikko5)
- [Käyttöohje](dokumentaatio/kayttoohje.md)

## Ohjeet

Asenna riippuvuudet:
```
poetry install
```

Käynnistä ohjelma:
```
poetry run invoke start
```

Aja testit:
```
poetry run invoke test
```

Testikattavuusraportti:
```
poetry run invoke coverage-report
```

Pylint-tarkistukset:
```
poetry run invoke lint
```


## Lisenssi
Sovellus käyttää D&D 5e Systems Reference Document (SRD 5.1) -materiaalia, joka on julkaistu Creative Commons Attribution 4.0 -lisenssillä.