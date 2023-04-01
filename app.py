import yugioh
import sqlite3
import random
import pprint

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
            self.hand1.pop(choiceOfCard)
            self.zone1.append(cardToSet)
        elif self.turn == 2:
            print (self.hand2)
            player1HandLength = len(self.hand2)
            choiceOfCard = int(input("Select a card to play: "))
            cardToSet = self.hand2[choiceOfCard]
            self.hand2.pop(choiceOfCard)
            self.zone2.append(cardToSet)
    
    def battle(self):
        if self.turn == 1:
            print (self.zone1)
            zone1Length = len(self.zone1)
            if (zone1Length > 0):
                choiceOfCard = int(input("Select a card to attack with: "))
                cardToAttackWith = self.zone1[choiceOfCard]
                if (len(self.zone2) > 0):
                    print (self.zone2)
                    choiceOfCard = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.zone2[choiceOfCard]
                    print ("{} attacks into {}".format(cardToAttackWith, cardToAttackInto))
                else:
                    print ("Direct Attack!")
                # select card
                # attack with card
            
        elif self.turn == 2:
            print (self.zone2)
            zone2Length = len(self.zone2)
            if (zone2Length > 0):
                choiceOfCard = int(input("Select a card to attack with: "))
                cardToAttackWith = self.zone2[choiceOfCard]
                if (len(self.zone1) > 0):
                    print (self.zone1)
                    choiceOfCard = int(input("Select a card to attack into: "))
                    cardToAttackInto = self.zone1[choiceOfCard]
                    print ("{} attacks into {}".format(cardToAttackWith, cardToAttackInto))
                else:
                    print ("Direct Attack!")
        
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