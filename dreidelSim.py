'''DreidelSim is a learning project using simulation. It is not meant to have broad use.
Author: chloemackay and bongotastic
'''

import random
import math

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

    def PlayGame(self):
        activePlayer = 0

        turn = 1

        while self.GameNotOver() or turn != 1000:
            result = self.SpinTheDreidel()

            if result == "Nun":
               pass
            elif result == "Shin":
                self.PlayerPutCoinOnTable(activePlayer)
            elif result == "Gimel":
                self.playerCoins[activePlayer] += self.coinTable
                self.coinTable = 0
                self.StartGame()
            elif result == "Hay":
                halfTable = math.floor(self.coinTable/2)
                self.playerCoins[activePlayer] += halfTable
                self.coinTable -= halfTable

            print(self.playerCoins)
            activePlayer += 1
            if activePlayer == len(self.playerCoins):
                activePlayer = 0
                turn += 1

        return turn



    def GameNotOver(self):
        for player in self.playerCoins:
            if player ==  sum(self.playerCoins):
                return False

        return True

    def SpinTheDreidel(self):
        dreidel = ["Gimel", "Shin", "Nun", "Hay"]
        return random.choice(dreidel)

if __name__ == "__main__":

    for i in range(1000):
        # create a game
        myGame = DreidelGame()
        myGame.StartGame()
        print(myGame.PlayGame())

