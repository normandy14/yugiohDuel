# Yugioh Duel :video_game:

## What is Yugioh Duel

Yugioh Duel is a small command line game modelling the Yugioh game (approximately year 2000).
Player controlls both players. Player can draw cards, set cards and change battle positions, do battle, and end turn.
Game ends when a player's life points reach zero.

## What this is About

### Python
This game uses extensive use of Python classes. This is a way to practice object-oriented programming in Python.

### Jupyter Notebook
This game uses a Jupyter Notebook to scrap data from two Yugioh deck .csv files. 
The .csv files were taken from [Yugi Starter Deck](https://yugioh.fandom.com/wiki/Starter_Deck:_Yugi)
and [Kaiba Starter Deck](https://yugioh.fandom.com/wiki/Starter_Deck:_Kaiba).
The decks were copies and pasted into a Google Sheet. Then downloaded as a.csv file. Then to a Jupyter notebook. The data from the Jupyter notebook was inserted into a SQLite3 database.

## Note

Spell and trap cards are not implemented because each spell and trap card's effect would have to be hard-coded for each code. 
As a result, monster cards implemented because the only significant properties are attack and defense points.
Effect-monsters are not implemented.

Modelling Yugioh Duel using approximately year 2000 was chosen because there are fewer effect cards, 
and modern elements of Yugioh such as XYZ summon and Pendelum cards are nonexistent 
-- as a result, making the mechanics and Yugioh easier to model in Yugioh Duel.

## Running the tests

Explain how to run the automated tests for this system:

```
pipenv run python3 testUnitTests.py -b
(or) python3 testUnitTests.py -b
```

### Implemented Technologies

Implentation of Yugioh Duel built with the following technologies:

* :snake: Python/Flask/Pipenv
* :floppy_disk: Git
* :notebook: Jupyter Notebook
* :cloud: SQLite3

## License

This project is licensed under the GNU General Public License v3.0 [License](LICENSE.md) - see the LICENSE.md file for details

## Authors

* :ocean: **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)
