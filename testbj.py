values = {"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,
          "ten":10,"jack":10,"queen":10,"king":10,"ace":1}
suits = ('Hearts', "Diamonds","Spades","Clubs")
ranks = ("two","three","four","five","six","seven","eight","nine",
          "ten","jack","queen","king","ace")


import random
from random import shuffle
class Deck:
     
    def __init__(self):
        self.listofcards = []
        for suit in suits:
            for rank in ranks:
                currentcard = Card(suit,rank)
                self.listofcards.append(currentcard)
                
    def shuffle(self):
        random.shuffle(self.listofcards)
        
    def deal_one(self):
        
        return self.listofcards.pop(0)
        
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Player:
    
    def __init__(self):       
        self.hand = []
        self.bankroll = 10

Dealer = Player()
DomBhai = Player()
GameDeck = Deck()
GameDeck.shuffle()

Dealer.hand.append(GameDeck.deal_one())
DomBhai.hand.append(GameDeck.deal_one())
Dealer.hand.append(GameDeck.deal_one())
DomBhai.hand.append(GameDeck.deal_one())

for x in DomBhai.hand:
    print(x)