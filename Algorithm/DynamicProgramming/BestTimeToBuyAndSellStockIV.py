# -*- coding: UTF-8 -*-

'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        if (k > len(prices)):
            profit = 0

            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                profit += (diff if diff > 0 else 0)
            return profit

        dpI0 = [0] * (k + 1)
        dpI1 = [-float('INF')] + [-prices[0]] * k
        for i in range(1, len(prices)):
            for k in range(1, k + 1):
                dpI0[k] = max(dpI0[k], dpI1[k] + prices[i])
                dpI1[k] = max(dpI1[k], dpI0[k - 1] - prices[i])
        return dpI0[k]


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[2,4,1], k=2))