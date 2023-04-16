import yugioh
import sqlite3
import random
import pprint

# ToDo:
# Attack card difference
# lifepoint deduction

# if lifepoint negative, current player takes damage
# if lifepoint positive, opponent playeer takes damage

# destroy defensive card if attk1 > attk2
# destroy both if equal
# destroy offensive if attk1 < attk2

class Card:
    # instance variables
    def __init__(self, cardName, position):
        self.cardName = cardName
        self.position = position

    def __repr__(self):
        return self.cardName

class Person:
    # instance variables
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.zone = []
        self.lifePoints = 8000
        self.loadHand()

    def loadHand(self):
       # print ("Load hand!")
       self.hand = self.deck[0:5]
       self.deck = self.deck[5:]

    def draw(self):
       nextCard = self.deck[:1]
       # print (self.hand)
       print (nextCard)
       self.hand = self.hand + nextCard
       print (self.hand)
       self.deck = self.deck[1:] # pop the last card from the deck

class Game:
    # instance variables
    def __init__(self, deck1, deck2):
        self.player1 = Person(deck1)
        self.player2 = Person(deck2)
        self.turn = 1

    def draw(self):
        print ("Draw time!")
        if self.turn == 1:
            self.player1.draw()
        elif self.turn == 2:
            self.player2.draw()

    def cardToSetWithPositionPlayer1(self):
        # Select card from hand
        player1HandLength = len(self.player1.hand)
        choiceOfCard = int(input("Select a card to play: "))
        cardToSet = self.player1.hand[choiceOfCard]
        # Combine position to set in with card
        positionToSetIn = int(input("Select 0 for attack or 1 for defense: "))
        self.player1.hand.pop(choiceOfCard)
        card = Card(cardToSet, positionToSetIn)
        return card

    # def combineCardWithPositionPlayer

    def cardToSetWithPositionPlayer2(self):
        layer1HandLength = len(self.player2.hand)
        choiceOfCard = int(input("Select a card to play: "))
        cardToSet = self.player2.hand[choiceOfCard]
        # position to set in
        positionToSetIn = int(input("Select 0 for attack or 1 for defense: "))
        self.player2.hand.pop(choiceOfCard)
        card = Card(cardToSet, positionToSetIn)
        return card

    def main(self):
        print ("Main Phase!")
        if self.turn == 1:
            card = self.cardToSetWithPositionPlayer1()
            self.player1.zone.append(card)
            # print (self.zone1)
        elif self.turn == 2:
            # print (self.player2.hand)
            card = self.cardToSetWithPositionPlayer2()
            self.player2.zone.append(card)
            # print (self.zone2)

    def battle(self):
        print ("Battle Phase!")
        if self.turn == 1:
            copyOfZone = self.player1.zone.copy()
            zone1Length = len(copyOfZone)
            while (zone1Length > 0):

                print (copyOfZone)

                choiceOfCardOffense = int(input("Select a card to attack with: "))
                cardToAttackWith = copyOfZone[choiceOfCardOffense]
                print (cardToAttackWith)

                if (len(self.player2.zone) > 0):
                    print (self.player2.zone)
                    choiceOfCardDefense = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.player2.zone[choiceOfCardDefense]
                    # print (cardToAttackInto)

                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    cardDefense = yugioh.get_card(card_name = cardToAttackInto)
                    lifePointDifference = cardOffense.attack - cardDefense.attack

                    if (lifePointDifference > 0):
                        self.player2.lifePoints -= lifePointDifference
                    elif (lifePointDifference < 0):
                        self.player1.lifePoints -= abs(lifePointDifference)

                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))

                    if (cardOffense.attack > cardDefense.attack):
                        self.player2.zone.pop(choiceOfCardDefense)
                    elif (cardOffense.attack == cardDefense.attack):
                        # both popped
                        self.player1.zone.pop(choiceOfCardOffense)
                        self.player2.zone.pop(choiceOfCardDefense)
                    else:
                        # cardOffense < cardDefense
                        self.player1.zone.pop(choiceOfCardOffense)
                else:
                    print ("Direct Attack!")
                    print (copyOfZone)
                    cardToAttackWith = copyOfZone[choiceOfCardOffense].cardName
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    self.player2.lifePoints -= cardOffense.attack
                # select card
                # attack with card
                copyOfZone.pop(choiceOfCardOffense)
                zone1Length -= 1


        elif self.turn == 2:
            copyOfZone = self.player2.zone.copy()
            zone2Length = len(self.player2.zone)
            while (zone2Length > 0):

                print (copyOfZone)

                choiceOfCardOffense = int(input("Select a card to attack with: "))
                cardToAttackWith = copyOfZone[choiceOfCardOffense]
                print (cardToAttackWith)

                if (len(self.player1.zone) > 0):
                    print (self.player1.zone)
                    choiceOfCardDefense = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.player1.zone[choiceOfCardDefense]
                    # print (cardToAttackInto)

                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    cardDefense = yugioh.get_card(card_name = cardToAttackInto)
                    lifePointDifference = cardOffense.attack - cardDefense.attack

                    if (lifePointDifference > 0):
                        self.player1.lifePoints -= lifePointDifference
                    elif (lifePointDifference < 0):
                        self.player2.lifePoints -= abs(lifePointDifference)

                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))
                    if (cardOffense.attack > cardDefense.attack):
                        # cardDefense popped
                         self.player1.zone.pop(choiceOfCardDefense)
                    elif (cardOffense.attack == cardDefense.attack):
                        # both popped
                        self.player2.zone.pop(choiceOfCardOffense)
                        self.player1.zone.pop(choiceOfCardDefense)
                    else:
                        # cardOffense < cardDefense
                        self.player2.zone.pop(choiceOfCardOffense)
                else:
                    print ("Direct Attack!")
                    print (copyOfZone)
                    cardToAttackWith = copyOfZone[choiceOfCardOffense].cardName
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    self.player1.lifePoints -= cardOffense.attack

                copyOfZone.pop(choiceOfCardOffense)
                zone2Length -= 1

        # print (self.turn)
        print ("player {} turn".format(self.turn))
        print (self.player1.zone)
        print (self.player2.zone)
        print ("P1 LP = {}".format(self.player1.lifePoints))
        print ("P2 LP = {}".format(self.player2.lifePoints))

    def end(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

# Functions for Game

def DeckSetup():
    # Setup for database
    conn = None
    try:
        conn = sqlite3.connect("Yugidb.db")
    except Error as e:
        print(e)

    cur = conn.cursor()

    cur.execute("SELECT name FROM deck1")
    rows = cur.fetchall()

    cur.execute("SELECT name FROM deck2")
    rows2 = cur.fetchall()

    # Setup the decks
    deck1 = [row[0] for row in rows]
    deck2 = [row[0] for row in rows2]

    # shuffle to two decks
    random.shuffle(deck1)
    random.shuffle(deck2)

    decks = [deck1, deck2]
    return decks


def main():
    decks = DeckSetup()
    deck1 = decks[0]
    deck2 = decks[1]
    game = Game(deck2, deck1)
    # pprint.pprint(deck1)

    # print (game.hand1)
    # print (game.hand2)

    game.draw()
    game.main()
    game.end()
    # game.firstTurn = False
    while (1 == 1):
        game.draw()
        game.main()
        game.battle()
        game.end()


if __name__ == "__main__":
    main()
