from deck import Deck
from players import Player
from dealer import Dealer
import random

class Dealers_Table:
    Pot = 0
    Cardsout = []
    def __init__(self, name, Dealer, *Players):
        self.name = name
        self.Round = 0
        self.Players = []
        self.Players.extend(Players)
    def RoundOrder(self):
        RO = 1
        if len(self.Players) == 4:
            RO = (f" {self.Players[0].name} is first \n {self.Players[1].name} is second \n {self.Players[2].name} is third \n {self.Players[3].name} is fourth")
        if len(self.Players) == 3:
            RO = (f"{self.Players[0].name} is first \n {self.Players[1].name} is second \n {self.Players[2].name} is third")
        if len(self.Players) == 2:
            RO = (f"{self.Players[0].name} is first \n {self.Players[1].name} is second")
        print(RO)
    def Play(self, Dealer, *Players):
        GAME = list(Players)
        Found = ""
        LST = []
        while Player.Game_Round < 6:
            print(f"This is Round {Player.Game_Round}! Place your bets!")
            while i < len(GAME) - 1:
                Bet = int(GAME[i].Betting(self))
                while Bet != 10 or Bet != 20:
                    Bet = int(GAME[i].Betting(self))
                Dealer.ShuffleNPass(Players)
                RoundOut = input("""Does anyone want to fold? \n (Note: Type their position #, one at a time:) If No-one folds, type NO: """)
                if RoundOut == str(NO):
                    pass
                elif RoundOut == str(1):
                    Found = GAME.pop(0)
                    LST.insert(Found)
                elif RoundOut == str(2):
                    Found = GAME.pop(1)
                    LST.insert(Found)
                elif RoundOut == str(3):
                    Found = GAME.pop(2)
                    LST.insert(Found)
                elif RoundOut == str(4):
                    Found = GAME.pop(3)
                    LST.insert(Found)
                
                i += 1

        


Ajani = Player("Ajani", 100, "Ajani's.txt")
Haley = Player("Haley", 100, "Haley's.txt")
Rahmir = Player("Rahmir", 100, "Rahmir's.txt")
Sandman = Player("Sandman", 100, "Sandman's.txt")
Tam = Dealer("Tam")
Disney = Deck("Disney", Joker=True)
Tam.EquipDeck(Disney)
Classic = Dealers_Table("Classic", Tam, Ajani, Haley, Rahmir, Sandman)
Classic.RoundOrder()

eval