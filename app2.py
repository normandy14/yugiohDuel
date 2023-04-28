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

UNITTEST = True
DEBUG = True

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

    # only at __init__
    def loadHand(self):
       # print ("Load hand!")
       self.hand = self.deck[0:5]
       self.deck = self.deck[5:]

    # draw from player's hand
    def draw(self):
       nextCard = self.deck[:1]
       # print (self.hand)
       print (nextCard)
       self.hand = self.hand + nextCard
       print (self.hand)
       self.deck = self.deck[1:] # pop the last card from the deck

class Game:
    # instance variables
    def __init__(self, deck1, deck2):# Destroy card(s) based on card attack points
        self.player1 = Person(deck1)
        self.player2 = Person(deck2)
        self.turn = 1

    # set a card from hand into the monster zone
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

    def cardToSetWithPositionPlayer2(self):
        layer1HandLength = len(self.player2.hand)
        choiceOfCard = int(input("Select a card to play: "))
        cardToSet = self.player2.hand[choiceOfCard]
        # position to set in
        positionToSetIn = int(input("Select 0 for attack or 1 for defense: "))
        self.player2.hand.pop(choiceOfCard)
        card = Card(cardToSet, positionToSetIn)
        return card

    def directAttackWithPlayer1(self, copyOfZone, choiceOfCardOffense):
        print ("Direct Attack!")
        print (copyOfZone)
        cardToAttackWith = copyOfZone[choiceOfCardOffense].cardName
        cardOffense = yugioh.get_card(card_name = cardToAttackWith)
        self.player2.lifePoints -= cardOffense.attack

    def directAttackWithPlayer2(self, copyOfZone, choiceOfCardOffense):
        print ("Direct Attack!")
        print (copyOfZone)
        cardToAttackWith = copyOfZone[choiceOfCardOffense].cardName
        cardOffense = yugioh.get_card(card_name = cardToAttackWith)
        self.player1.lifePoints -= cardOffense.attack

    # For attacking into monster in attack mode
    def calculateLifePointsOffensePlayer1(self, cardOffense, cardDefense):
        lifePointDifference = cardOffense.attack - cardDefense.attack

        if (lifePointDifference > 0):
            self.player2.lifePoints -= lifePointDifference
        elif (lifePointDifference < 0):
            self.player1.lifePoints -= abs(lifePointDifference)
        return lifePointDifference

    def calculateLifePointsOffensePlayer2(self, cardOffense, cardDefense):
        lifePointDifference = cardOffense.attack - cardDefense.attack

        if (lifePointDifference > 0):
            self.player1.lifePoints -= lifePointDifference
        elif (lifePointDifference < 0):
            self.player2.lifePoints -= abs(lifePointDifference)
        return lifePointDifference

    # on player 1's turn
    # cardOffense and cardDefense are the acutal object from yugioh 3rd party

    # choiceOfCardOffense and choiceOfCardDefense defense are the positions of
    # the cards attacking and defending on each player1s monster zone, respectively
    # (the latter two are only used when the yugioh card object is destroyed
    # to "pop" the destroyed card on the field)
    def destroyMonsterZoneOffensivePlayer1(self, cardOffense, cardDefense, choiceOfCardOffense, choiceOfCardDefense):
        if (cardOffense.attack > cardDefense.attack):
            self.player2.zone.pop(choiceOfCardDefense)
        elif (cardOffense.attack == cardDefense.attack):
            # both popped
            self.player1.zone.pop(choiceOfCardOffense)
            self.player2.zone.pop(choiceOfCardDefense)
        else:
            # cardOffense < cardDefense
            self.player1.zone.pop(choiceOfCardOffense)

    # on player 2's turn
    def destroyMonsterZoneOffensivePlayer2(self, cardOffense, cardDefense, choiceOfCardOffense, choiceOfCardDefense):
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

    def draw(self):
        print ("Draw time!")
        if self.turn == 1:
            self.player1.draw()
        elif self.turn == 2:
            self.player2.draw()

    def main(self):
        print ("Main Phase!")
        if self.turn == 1:
            # select the card to set to monster zone from hand and select its card position
            card = self.cardToSetWithPositionPlayer1()
            self.player1.zone.append(card)
            # print (self.zone1)
        elif self.turn == 2:
            card = self.cardToSetWithPositionPlayer2()
            self.player2.zone.append(card)

    def battle(self):
        print ("Battle Phase!")
        if self.turn == 1:
            copyOfZone = self.player1.zone.copy()
            zone1Length = len(copyOfZone)
            # while there are monster cards on the player 1's fielfs
            while (zone1Length > 0):
                # To show all possible cards to attack with on player 1's field
                print (copyOfZone)

                # select a card to attack with
                ### SOLVE LATER: assumes all cards in player 1's field are in attack position (cards in defense position)
                choiceOfCardOffense = int(input("Select a card to attack with: "))
                cardToAttackWith = copyOfZone[choiceOfCardOffense]

                if DEBUG: print (cardToAttackWith)

                # if there are monster cards on player 2's field -- or cannot direct attack
                if (len(self.player2.zone) > 0):
                    # show all posible cards on player 2's fierd that can be targetted by player 1's monster cards
                    print (self.player2.zone)

                    choiceOfCardDefense = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.player2.zone[choiceOfCardDefense]

                    # if DEBUG (print (cardToAttackInto))

                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    cardDefense = yugioh.get_card(card_name = cardToAttackInto)

                    # calculate lifepoint difference
                    lifePointDifference = self.calculateLifePointsOffensePlayer1(cardOffense, cardDefense)
                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))

                    # Destroy card(s) based on card attack points
                    # SOLVE LATTER: can create class called 'Attack Object', that has cardOffense, cardDefense, choiceOfCardOffense, choiceOfCardDefense
                    self.destroyMonsterZoneOffensivePlayer1(cardOffense, cardDefense, choiceOfCardOffense, choiceOfCardDefense)

                else:
                    # A direct Attack
                    self.directAttackWithPlayer1(copyOfZone, choiceOfCardOffense)

                # A substiutue for adding "used" property in Card class __init__
                # the attacking card on player 1's monster zone has been used
                # and no longer can be used, so we "pop" from the copy
                copyOfZone.pop(choiceOfCardOffense)
                zone1Length -= 1 # a card was selected and then used, so the cards that are still avaliable are -1

        elif self.turn == 2:
            copyOfZone = self.player2.zone.copy()
            zone2Length = len(self.player2.zone)
            while (zone2Length > 0):

                if DEBUG: print (copyOfZone)

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

                    # calculate lifepoint difference
                    lifePointDifference = self.calculateLifePointsOffensePlayer2(cardOffense, cardDefense)
                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))

                    # Destroy card(s) based on card attack points (could have used lifepoint difference)
                    self.destroyMonsterZoneOffensivePlayer2(cardOffense, cardDefense, choiceOfCardOffense, choiceOfCardDefense)
                else:
                    # A direct Attack
                    self.directAttackWithPlayer2(copyOfZone, choiceOfCardOffense)

                # A substiutue for adding "used" property in Card class __init__s
                copyOfZone.pop(choiceOfCardOffense)
                zone2Length -= 1

        # alot of DEBUG statements
        # print (self.turn)
        if DEBUG: print ("player {} turn".format(self.turn))
        if DEBUG: print (self.player1.zone)
        if DEBUG: print (self.player2.zone)
        if DEBUG: print ("P1 LP = {}".format(self.player1.lifePoints))
        if DEBUG: print ("P2 LP = {}".format(self.player2.lifePoints))

    def end(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

# Functions for Game

def deckSetup():
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

    # print (deck1)
    # print (deck2)

    # shuffle the two decks
    if UNITTEST == False:
        random.shuffle(deck1)
        random.shuffle(deck2)

    decks = [deck1, deck2]
    return decks


def main():
    decks = deckSetup()
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
    while (True):
        game.draw()
        game.main()
        game.battle()
        game.end()


if __name__ == "__main__":
    main()
