from typing import List

"""
    This class to calculate the Maximum money a player can win in a Game of Coins.
"""

"""
p[i][j] = 
0: i + 1, j - 1
1: i + 2, j
2: i, j - 2
3: i
4: j
"""


class Coins:
    def __init__(self, coins: List[int]):
        self.coins = coins
        # Creating 2D array with the length of our coins array. This 2D array will be our dynamic table.
        self.dp = [[0 for _ in range(len(coins))] for _ in range(len(coins))]
        self.p = [[-1 for _ in range(len(coins))] for _ in range(len(coins))]

    # This function is created to go through the array and find the optimal solution for each index.
    def maximum_money(self):
        # This loop to add the initial value to the dp table when row's value equals the column's
        for i in range(len(self.coins)):
            self.dp[i][i] = self.coins[i]

        # This loop to determine the maximum when we have only 2 values
        for i in range(len(self.coins) - 1):
            if self.coins[i] > self.coins[i + 1]:
                self.dp[i][i + 1] = self.coins[i]
                self.p[i][i + 1] = 3
            else:
                self.dp[i][i + 1] = self.coins[i + 1]
                self.p[i][i + 1] = 4

        # This loop to go through all the dp table to calculate the final answer
        for i in range(len(self.coins) - 3, -1, -1):
            for j in range(2, len(self.coins)):
                self.__maximum_coins(i, j)

    # This function to calculate the values of a certain index in the dp table based on the dynamic formula
    def __maximum_coins(self, i, j):
        if i > j:
            self.dp[i][j] = 0
        else:
            max_i = self.coins[i] + min(self.dp[i + 1][j - 1], self.dp[i + 2][j])
            max_j = self.coins[j] + min(self.dp[i + 1][j - 1], self.dp[i][j - 2])
            # To check which path we used to get the answer to determine later which coins the player used
            # to get to the final answer
            if max_i > max_j:
                self.dp[i][j] = max_i
                if self.dp[i + 1][j - 1] < self.dp[i + 2][j]:
                    self.p[i][j] = 0
                else:
                    self.p[i][j] = 1
            else:
                self.dp[i][j] = max_j
                if self.dp[i + 1][j - 1] < self.dp[i][j - 2]:
                    self.p[i][j] = 0
                else:
                    self.p[i][j] = 2

    # This function returns the dynamic table
    def get_table(self):
        return self.dp

    # This function used to trace the path of coins the player used to get to the final answer, if the path is 0 means
    # the move on the dp table was i + 1, j - 1. If path is 1 means the move on the dp table was i + 2, j, if the path
    # is 2 means the move is i, j - 2. Any other value means we've reached the end, so we break out of the loop
    def get_moves(self):
        moves = []
        # Checks if the input is empty
        if not self.coins:
            return moves
        i = 0
        j = len(self.coins) - 1
        res = self.dp[0][-1]

        # This loop goes through the path and the dp table arrays to get the moves based on the selected answer in each
        # move used to get to the final answer
        while True:
            # checks if the move we've taken is i + 1, j -1
            if self.p[i][j] == 0:
                if res - self.coins[i] == self.dp[i + 1][j - 1]:
                    moves.append(self.coins[i])
                    res -= self.coins[i]
                else:
                    moves.append((self.coins[j]))
                    res -= self.coins[j]
                i += 1
                j -= 1
            # checks if the move we,ve taken is i +2, j
            elif self.p[i][j] == 1:
                if res - self.coins[i] == self.dp[i + 2][j]:
                    moves.append(self.coins[i])
                    res -= self.coins[i]
                else:
                    moves.append((self.coins[j]))
                    res -= self.coins[j]
                i += 2
            # checks if the move we,ve taken is i, j - 2
            elif self.p[i][j] == 2:
                if res - self.coins[i] == self.dp[i][j - 2]:
                    moves.append(self.coins[i])
                    res -= self.coins[i]
                else:
                    moves.append((self.coins[j]))
                    res -= self.coins[j]
                j -= 2
            # Any other possibility means we've reached the end, we take the final value and break from the loop
            else:
                if res - self.coins[i] == 0:
                    moves.append(self.coins[i])
                    res -= self.coins[i]
                elif res - self.coins[j] == 0:
                    moves.append((self.coins[j]))
                    res -= self.coins[j]
                break

        return moves
