# -*- coding: UTF-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

from typing import List
class Solution: # 和Solution2的区别在于对状态的不同定义！
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])
            dp[i][2] = dp[i-1][0]

        return max(dp[len(prices)-1][0], dp[len(prices)-1][2])

from typing import List
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float('-inf')

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]

        return max(dp[len(prices)-1][0], dp[len(prices)-1][2])

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            if i - 2 < 0:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], 0 - prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return max(dp[len(prices)-1][0], dp[len(prices)-1][2])

class Solution4: # 压缩Solution3空间复杂度
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        dp_i_0, dp_i_1 = 0, -prices[0]
        dp_pre_0 = 0

        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp

        return dp_i_0

if __name__ == "__main__":
    print(Solution4().maxProfit(prices=[2,1,4]))