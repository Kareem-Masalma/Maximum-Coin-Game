from typing import List

"""
    This class to calculate the Maximum money a player can win in a Game of Coins.
"""


class Coins:
    def __init__(self, coins: List[int]):
        self.coins = coins
        # Creating 2D array with the length of our coins array. This 2D array will be our dynamic table.
        self.dp = [[0 for _ in range(len(coins))] for _ in range(len(coins))]
        self.moves = []  # This array will store the moves of each player

    # This function is created to go through the array and find the optimal solution for each index.
    def maximum_money(self):
        for i in range(len(self.coins)):
            self.dp[i][i] = self.coins[i]

        for i in range(len(self.coins) - 1):
            self.dp[i][i + 1] = max(self.coins[i], self.coins[i + 1])

        for i in range(len(self.coins) - 3, -1, -1):
            for j in range(2, len(self.coins)):
                self.maximum_coins(i, j)

    def maximum_coins(self, i, j):
        if i > j:
            self.dp[i][j] = 0
        else:
            self.dp[i][j] = max(self.coins[i] + min(self.dp[i + 1][j - 1], self.dp[i + 2][j]),
                                self.coins[j] + min(self.dp[i + 1][j - 1], self.dp[i][j - 2]))

    def get_table(self):
        return self.dp

    # def get_moves(self):
    #     i = 0
    #     j = len(self.coins) - 1
    #     res = self.dp[0][-1]
    #     while i < len(self.coins) and j >= 0:

