if self.turn == 1:
        copyOfZone = self.player1.zone
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
