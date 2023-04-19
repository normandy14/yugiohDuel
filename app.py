import yugioh
import sqlite3
import random
import pprint

# ToDo:

# else cardAttackInto is 1 (defense position)
# if attackOfSame < defenseOfOther, then take lifepoint damage to current player with lp difference
# if attackOfSame > defenseOfOther, defensive card is destroyed, but lp damage is 0

class Card:
    # instance variables
    def __init__(self, cardName, position):
        self.cardName = cardName
        self.position = position
    
    def __repr__(self):
        return self.cardName

class Game:
    # instance variables
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.hand1 = []
        self.hand2 = []
        self.loadHands()
        self.turn = 1
        self.zone1 = []
        self.zone2 = []
        self.lifePointsP1 = 8000
        self.lifePointsP2 = 8000
        # self.firstTurn = True
    
    def draw(self):
        print ("Draw time!")
        if self.turn == 1:
            self.hand1 = self.hand1 + self.deck1[:1]
            self.deck1 = self.deck1[1:]
        elif self.turn == 2:
            self.hand2 = self.hand2 + self.deck2[:1]
            self.deck2 = self.deck2[1:]
    
    def main(self):
        print ("Main Phase!")
        if self.turn == 1:
            print (self.hand1)
            player1HandLength = len(self.hand1)
            choiceOfCard = int(input("Select a card to play: "))
            cardToSet = self.hand1[choiceOfCard]
            # position to set in
            positionToSetIn = int(input("Select 0 for attack or 1 for defense: "))
            self.hand1.pop(choiceOfCard)
            card = Card(cardToSet, positionToSetIn)
            self.zone1.append(card)
            # print (self.zone1)
        elif self.turn == 2:
            print (self.hand2)
            player1HandLength = len(self.hand2)
            choiceOfCard = int(input("Select a card to play: "))
            cardToSet = self.hand2[choiceOfCard]
            # position to set in
            positionToSetIn = int(input("Select 0 for attack or 1 for defense: "))
            self.hand2.pop(choiceOfCard)
            card = Card(cardToSet, positionToSetIn)
            self.zone2.append(card)
            # print (self.zone2)
    
    def battle(self):
        if self.turn == 1:
            print (self.zone1)
            zone1Length = len(self.zone1)
            if (zone1Length > 0):
                choiceOfCardOffense = int(input("Select a card to attack with: "))
                cardToAttackWith = self.zone1[choiceOfCardOffense]
                print (cardToAttackWith)
                print (cardToAttackWith.position)
                if (len(self.zone2) > 0):
                    print (self.zone2)
                    choiceOfCardDefense = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.zone2[choiceOfCardDefense]
                    print (cardToAttackInto.position)
                    # print (cardToAttackInto)
                    
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    cardDefense = yugioh.get_card(card_name = cardToAttackInto)
                    lifePointDifference = cardOffense.attack - cardDefense.attack
                    
                    if (lifePointDifference > 0):
                        self.lifePointsP2 -= lifePointDifference
                    elif (lifePointDifference < 0):
                        self.lifePointsP1 -= abs(lifePointDifference)
                    
                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))
                    
                    if (cardOffense.attack > cardDefense.attack):
                        self.zone2.pop(choiceOfCardDefense)
                    elif (cardOffense.attack == cardDefense.attack):
                        # both popped
                        self.zone1.pop(choiceOfCardOffense)
                        self.zone2.pop(choiceOfCardDefense)
                    else:
                        # cardOffense < cardDefense 
                        self.zone1.pop(choiceOfCardOffense)
                else:
                    print ("Direct Attack!")
                    cardToAttackWith = self.zone1[choiceOfCardOffense].name
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    self.lifePointsP2 -= cardOffense.attack
                # select card
                # attack with card
              
            
        elif self.turn == 2:
            print (self.zone2)
            zone2Length = len(self.zone2)
            if (zone2Length > 0):
                choiceOfCardOffense = int(input("Select a card to attack with: "))
                cardToAttackWith = self.zone2[choiceOfCardOffense]
                print (cardToAttackWith.position)
                # print (cardToAttackWith)
                if (len(self.zone1) > 0):
                    print (self.zone1)
                    choiceOfCardDefense = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.zone1[choiceOfCardDefense]
                    print (cardToAttackInto.position)
                    # print (cardToAttackInto)
                    
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    cardDefense = yugioh.get_card(card_name = cardToAttackInto)
                    lifePointDifference = cardOffense.attack - cardDefense.attack
                    
                    if (lifePointDifference > 0):
                        self.lifePointsP1 -= lifePointDifference
                    elif (lifePointDifference < 0):
                        self.lifePointsP2 -= abs(lifePointDifference)
                    
                    print ("{} attacks into {} for {} damage".format(cardToAttackWith, cardToAttackInto, lifePointDifference))
                    if (cardOffense.attack > cardDefense.attack):
                        # cardDefense popped
                         self.zone1.pop(choiceOfCardDefense)
                    elif (cardOffense.attack == cardDefense.attack):
                        # both popped
                        self.zone2.pop(choiceOfCardOffense)
                        self.zone1.pop(choiceOfCardDefense)
                    else:
                        # cardOffense < cardDefense 
                        self.zone2.pop(choiceOfCardOffense)
                        
                        
                    
                else:
                    print ("Direct Attack!")
                    cardToAttackWith = self.zone2[choiceOfCardOffense].name
                    cardOffense = yugioh.get_card(card_name = cardToAttackWith)
                    self.lifePointsP1 -= cardOffense.attack
               
        
        # print (self.turn)
        print ("player {} turn".format(self.turn))
        print (self.zone1)
        print (self.zone2)
        print ("P1 LP = {}".format(self.lifePointsP1))
        print ("P2 LP = {}".format(self.lifePointsP2))
        
    def end(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
    
    def loadHands(self):
        self.hand1 = self.deck1[0:5]
        self.hand2 = self.deck2[0:5]
        
        self.deck1 = self.deck1[5:]
        self.deck2 = self.deck2[5:]
            
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
    game = Game(deck1, deck2)
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