from random import randint
class Deck:
    Cards = {
        "Ace of Spades" : 1,
        "Ace of Hearts" : 1,
        "Ace of Diamonds" : 1,
        "Ace of Clubs" : 1,
        "2 of Clubs" : 1,
        "3 of Clubs" : 1,
        "4 of Clubs" : 1,
        "5 of Clubs" : 1,
        "6 of Clubs" : 1,
        "7 of Clubs" : 1, 
        "8 of Clubs" : 1,
        "9 of Clubs" : 1,
        "10 of Clubs" : 1,
        "Jack of Clubs" : 1,
        "Queen of Clubs" : 1,
        "King of Clubs" : 1,
        "2 of Diamonds" : 1,
        "3 of Diamonds" : 1,
        "4 of Diamonds" : 1,
        "5 of Diamonds" : 1,
        "6 of Diamonds" : 1,
        "7 of Diamonds" : 1,
        "8 of Diamonds" : 1, 
        "9 of Diamonds" : 1,
        "10 of Diamonds" : 1,
        "Jack of Diamonds" : 1,
        "Queen of Diamonds" : 1,
        "King of Diamonds" : 1,
        "2 of Hearts" : 1,
        "3 of Hearts" : 1,
        "4 of Hearts" : 1,
        "5 of Hearts" : 1,
        "6 of Hearts" : 1,
        "7 of Hearts" : 1,
        "8 of Hearts" : 1,
        "9 of Hearts" : 1,
        "10 of Hearts" : 1,
        "Jack of Hearts" : 1,
        "Queen of Hearts" : 1,
        "King of Hearts" : 1,
        "2 of Spades" : 1,
        "3 of Spades" : 1,
        "4 of Spades" : 1,
        "5 of Spades" : 1,
        "6 of Spades" : 1,
        "7 of Spades" : 1,
        "8 of Spades" : 1,
        "9 of Spades" : 1,
        "10 of Spades" : 1,
        "Jack of Spades" : 1,
        "Queen of Spades" : 1,
        "King of Spades" : 1}
    def __init__(self, name, Joker = False):
        self.name = name
        self.Joker = Joker
    def add_Joker(self):
        self.Joker = True
        if self.Joker == True:
            self.Cards["Joker"] = 1
    def no_more_Joker(self):
        self.Joker = False
        if self.Joker == False:
            del self.Cards["Joker"]

        








        
