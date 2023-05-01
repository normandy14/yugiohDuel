from unittest import mock
from unittest import TestCase
import unittest
from app2 import *

class deckSetupTests(TestCase):
    def setUp(self):
        self.result = deckSetup()

    def testDeckSetupDeck1(self):
        result = self.result[0]
        self.assertEqual(result, ['Blue-Eyes White Dragon', 'Hitotsu-Me Giant', 'Ryu-Kishin', 'The Wicked Worm Beast', 'Battle Ox', 'Koumori Dragon', 'Judge Man', 'Rogue Doll', 'Kojikocy', 'Uraby', 'Gyakutenno Megami', 'Mystic Horseman', 'Terra the Terrible', 'Dark Titan of Terror', 'Dark Assailant', 'Master & Expert', 'Unknown Warrior of Fiend', 'Mystic Clown', 'Ogre of the Black Shadow', 'Dark Energy', 'Invigoration', 'Dark Hole', 'Ookazi', 'Ryu-Kishin Powered', 'Swordstalker', 'La Jinn the Mystical Genie of the Lamp', 'Rude Kaiser', 'Destroyer Golem', 'Skull Red Bird', 'D. Human', 'Pale Beast', 'Fissure', 'Trap Hole', 'Two-Pronged Attack', 'De-Spell', 'Monster Reborn', 'The Inexperienced Spy', 'Reinforcements', 'Ancient Telescope', 'Just Desserts', 'Lord of D.', 'The Flute of Summoning Dragon', 'Mysterious Puppeteer', 'Trap Master', 'Sogen', 'Hane-Hane', 'Reverse Trap', 'Remove Trap', 'Castle Walls', 'Ultimate Offering'])

    def testDeckSetupDeck2(self):
        result = self.result[1]
        self.assertEqual(result, ['Mystical Elf', 'Feral Imp', 'Winged Dragon, Guardian of the Fortress #1', 'Summoned Skull', 'Beaver Warrior', 'Dark Magician', 'Gaia The Fierce Knight', 'Curse of Dragon', 'Celtic Guardian', 'Mammoth Graveyard', 'Great White', 'Silver Fang', 'Giant Soldier of Stone', 'Dragon Zombie', 'Doma The Angel of Silence', 'Ansatsu', 'Witty Phantom', 'Claw Reacher', 'Mystic Clown', 'Sword of Dark Destruction', 'Book of Secret Arts', 'Dark Hole', 'Dian Keto the Cure Master', 'Ancient Elf', 'Magical Ghost', 'Fissure', 'Trap Hole', 'Two-Pronged Attack', 'De-Spell', 'Monster Reborn', 'Reinforcements', 'Change of Heart', 'The Stern Mystic', 'Wall of Illusion', 'Neo the Magic Swordsman', 'Baron of the Fiend Sword', 'Man-Eating Treasure Chest', 'Sorcerer of the Doomed', 'Last Will', 'Waboku', 'Soul Exchange', 'Card Destruction', 'Trap Master', 'Dragon Capture Jar', 'Yami', 'Man-Eater Bug', 'Reverse Trap', 'Remove Trap', 'Castle Walls', 'Ultimate Offering'])

class testDrawPhase(TestCase):
    def setUp(self):
        decks = deckSetup()
        deck1 = decks[0]
        deck2 = decks[1]
        self.game = Game(deck2, deck1)

    def testDrawPhase1(self):
        self.game.draw()
        result = self.game.player1.hand[-1]
        self.assertEqual(result, "Dark Magician")

    def testDrawPhase2(self):
        self.game.draw()
        self.game.end()
        self.game.draw()
        result = self.game.player2.hand[-1]
        self.assertEqual(result, "Koumori Dragon")

'''
class dictCreateTests(TestCase):
    @mock.patch('module_under_test.input', create=True)
    def testDictCreateSimple(self, mocked_input):
        mocked_input.side_effect = ['Albert Einstein', '42.81', 'done']
        result = module_under_test.dictCreate(1)
        self.assertEqual(result, {'Albert Einstein': [42.81]})
'''

if __name__ == '__main__':
    unittest.main()
