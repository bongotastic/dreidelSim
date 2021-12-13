'''DreidelSim is a learning project using simulation. It is not meant to have broad use.
Author: chloemackay and bongotastic
'''

import random
import math

class DreidelGame:
    def __init__(self, numPlayer, startCoin):
        # The number of coins on the table
        self.coinTable = 0

        # Each player's coins
        self.playerCoins = []
        for i in range(numPlayer):
            self.playerCoins.append(startCoin)

        self.dreidelSpin = 0

    def PlayerPutCoinOnTable(self, playerIndex):
        if self.playerCoins[playerIndex] > 0:
            # Take away one coin
            self.playerCoins[playerIndex] -= 1

            # Add coin to the table
            self.coinTable += 1
        else:
            self.playerCoins[playerIndex] = -1

    def StartGame(self):
        for i in range(len(self.playerCoins)):
            self.PlayerPutCoinOnTable(i)

    def PlayGame(self):
        activePlayer = 0

        turn = 1

        while self.GameNotOver():

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

            activePlayer += 1
            if activePlayer == len(self.playerCoins):
                while -1 in self.playerCoins:
                    self.playerCoins.remove(-1)
                activePlayer = 0
                turn += 1

        return self.PlayTime()



    def GameNotOver(self):
        if len(self.playerCoins) != 1:
            return True

        return False

    def SpinTheDreidel(self):
        self.dreidelSpin += 1
        dreidel = ["Gimel", "Shin", "Nun", "Hay"]
        return random.choice(dreidel)

    def PlayTime(self):
        return 9 * self.dreidelSpin


def RunExperiment(replicate, numPlayer, numCoins):
    totalTime = 0
    for i in range(replicate):
        # create a game
        myGame = DreidelGame(numPlayer, numCoins)
        myGame.StartGame()
        totalTime += myGame.PlayGame()

    return float(totalTime)/float(replicate)

if __name__ == "__main__":

    numPlayer = 2

    for numCoins in range(1, 20):
        averageTime = RunExperiment(1000, numPlayer, numCoins)
        print("coin = %d   average=%f"%(numCoins ,averageTime))


