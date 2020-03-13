# -*- coding: UTF-8 -*-

'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''

from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                if i < coin: continue
                dp[i] += dp[i - coin]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().change(amount=4, coins=[1,2,3]))