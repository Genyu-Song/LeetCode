# -*- coding: UTF-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit, profit = 0, 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit

class Solution2(object):
    def maxProfit(self, prices):
        try:
            minprice, maxprofit = prices[0], 0
            for i in prices[1:]:
                if i > minprice and i - minprice > maxprofit:
                    maxprofit = i - minprice
                elif i < minprice:
                    minprice = i
        except: maxprofit = 0
        return maxprofit

class Solution3(object): # Dynamic Programming
    def maxProfit(self, prices):
        try:
            diff = []
            for i in range(0, len(prices)-1):
                diff.append(prices[i+1] - prices[i])
            dp = [[] for i in range(len(prices)-1)]
            dp[0] = max(0, diff[0])
            for i in range(1, len(dp)):
                dp[i] = max(0, dp[i-1] + diff[i])
            return max(dp)
        except:
            return 0

if __name__ == '__main__':
    print(Solution3().maxProfit(prices=[1,2]))