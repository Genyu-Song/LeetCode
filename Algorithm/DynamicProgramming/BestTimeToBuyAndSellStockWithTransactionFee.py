# -*- coding: UTF-8 -*-

'''
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        dp_i_0 = 0
        dp_i_1 = - prices[0] - fee

        for i in range(1, N):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)

        return dp_i_0

if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1,3,2,8,4,9], fee=2))