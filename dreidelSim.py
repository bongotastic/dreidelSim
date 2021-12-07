'''DreidelSim is a learning project using simulation. It is not meant to have broad use.
Author: chloemackay and bongotastic
'''

class DreidelGame:
    def __init__(self):
        # The number of coins on the table
        self.coinTable = 0

        # Each player's coins
        self.playerCoins = [5,5,5,5,5]

    def PlayerPutCoinOnTable(self, playerIndex):
        # Take away one coin
        self.playerCoins[playerIndex] -= 1

        # Add coin to the table
        self.coinTable += 1

    def StartGame(self):
        for i in range(len(self.playerCoins)):
            self.PlayerPutCoinOnTable(i)

if __name__ == "__main__":
    # create a game
    myGame = DreidelGame()

    myGame.StartGame()

    print(myGame)