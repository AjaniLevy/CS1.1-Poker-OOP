from players import Player
from deck import Deck
import random
from random import choices
class Dealer(Player):
    DealersHand = []
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        self.pDeck = []

    def Betting(self, amount):
        pass
    def Fold(self):
        pass
    def EquipDeck(self, Deck):
        self.pDeck = Deck
        for key, value in self.pDeck.Cards.items():
            self.DealersHand.append(key)
    def ShuffleNPass(self, *Players):
            for Player in Players:
                Reset = self.DealersHand
                Pass = choices(Reset, k=2)
                self.DealersHand.remove(Pass[0])
                self.DealersHand.remove(Pass[1])
                Player.pDeck.extend(Pass)

    def Flop(self, Table):
        Reset = self.DealersHand
        Pass = choices(Reset, k=3)
        for i in range(3):
            self.DealersHand.remove(Pass[i])
        Table.Cardsout.extend(Pass)
        
    def Turn_and_River(self, Table):
        Reset = self.DealersHand
        Pass = choices(Reset, k=1)
        self.DealersHand.remove(Pass)
        Table.Cardsout.extend(Pass)



        

Ajani = Player("Ajani")
Tam = Dealer("Tam")
Suite = Deck("Suite")
Tam.EquipDeck(Suite)
Tam.ShuffleNPass(Ajani)




