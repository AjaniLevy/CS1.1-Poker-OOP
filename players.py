class Player:
    Game_Round = 1
    GroupChips = 300

    def __init__(self, name, Chips=0, page =""):
        self.playing = False
        self.name = name
        self.Chips = Chips
        self.pDeck = []
        self.page = page
    def Betting(self, Table):
        Bet = 0
        amount = int(input(f"How much do you want to bet, {self.name}? " ))
        if self.Chips > amount and Bet == 10 or Bet == 20:
            self.Chips = self.Chips - amount
            Table.Pot += amount
        else:
            print (f"{self.name} cannot bet {amount} amount")
    def Fold(self, Table):
        self.playing = False
    def CalculateIndividualChips(self):
        number = int(input("How many players are expected?" ))
        answer = self.GroupChips // number
        print(f"Each Player will recieve {answer} Chips")
    def CheckPage(self, DealerTable=0):
        x = not isinstance(DealerTable, int)
        if x == True:
            Counter = 0
            CARDL = len(DealerTable.Cardsout)
            CARDS = range(CARDL-1)
            with open(self.page, "w") as outfile:
                outfile.write(f"The POT is at {DealerTable.Pot} \n")
                while Counter < CARDL:
                    outfile.write(f"Card: {DealerTable.Cardsout[CARDS[Counter]]}")
                    Counter += 1
        with open(self.page, "w") as outfile:
            outfile.write(f"Your Cards: {self.pDeck[0]} and {self.pDeck[1]}\n")
            outfile.write(f"Your Chips: {self.Chips} \n")
            outfile.write(f"Round: {self.Game_Round}")
    @classmethod
    def Next_Round(cls):
        cls.Game_Round += 1






    
    







