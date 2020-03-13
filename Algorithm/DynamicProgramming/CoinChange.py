# -*- coding: UTF-8 -*-

'''
#322
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort(reverse=True)
        memo = {amount: 0}
        stack = [amount]
        count = 0
        while stack:
            if 0 in stack:
                return memo[0]
            target = stack.pop(0)
            for coin in coins:
                residue = target - coin
                if residue not in memo:
                    if residue >= 0:
                        memo[residue] = memo[target] + 1
                        stack.append(residue)
        return -1

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    print(Solution2().coinChange(coins=[1,3,5], amount=11))