'''DreidelSim is a learning project using simulation. It is not meant to have broad use.
Author: chloemackay and bongotastic
'''

class DreidelGame:
    def __init__(self):
        # The number of coins on the table
        self.coinTable = 0

        # Each player's coins
        self.playerCoins = [5,5,5,5,5]