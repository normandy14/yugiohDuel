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
    
    def loadHands(self):
        self.hand1 = self.deck1[0:5]
        self.hand2 = self.deck2[0:5]
        
        self.deck1 = self.deck1[5:]
        self.deck2 = self.deck2[5:]
    
    def draw(self):
        if self.turn == 1:
            self.hand1 = self.hand1 + self.deck1[:1]
            self.deck1 = self.deck1[1:]
        elif self.turn == 2:
            self.hand2 = self.hand2 + self.deck2[:1]
            self.deck2 = self.deck2[1:]
    
    def endTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
            
    def setCardToZone(self):
        userInput = -1
        if self.turn == 1:
            print (self.hand1)
            lengthOfHand = len(self.hand1) - 1
            # print (lengthOfHand)
            while (userInput >= lengthOfHand or userInput < 0):
                print ("select from 0 to {}".format(lengthOfHand))
                userInput = int(input("Select card to play: "))
                print (self.hand1[userInput])
        elif self.turn == 2:
            print (self.hand2)
            lengthOfHand = len(self.hand2) - 1
            # print (lengthOfHand)
            while (userInput >= lengthOfHand or userInput < 0):
                print ("select from 0 to {}".format(lengthOfHand))
                userInput = int(input("Select card to play: "))
                print (self.hand2[userInput])
        
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
    # print (game.hand1)
    game.setCardToZone()
    game.endTurn()
    game.draw()
    # print (game.hand2)
    game.setCardToZone()
    game.endTurn()
    

if __name__ == "__main__":
    main()
    
   
# read from SQLite3 to list
# shuffle (randomize) list

# create 2 hands
# Draw on your turn
# end turn

# Draw on opponnet turn
# end opponent turn

# start your turn
# draw 1 card

# end your turn
# start opponent turn 
# end opponent turn