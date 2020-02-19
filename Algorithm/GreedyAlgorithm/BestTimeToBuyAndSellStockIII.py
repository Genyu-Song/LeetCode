# -*- coding: UTF-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0

        # dp[ith][hold][#sell]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')

        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = max(dp[i-1][1][0]+prices[i], dp[i-1][0][1]) # 可能是今天卖出，或是前几天卖出
            dp[i][0][2] = max(dp[i-1][1][1]+prices[i], dp[i-1][0][2])
            dp[i][1][0] = max(dp[i-1][0][0]-prices[i], dp[i-1][1][0]) # 可能是今天买入，或是前几天买入
            dp[i][1][1] = max(dp[i-1][0][1]-prices[i], dp[i-1][1][1])
            dp[i][1][2] = float('-inf')

        return max(dp[len(prices)-1][0][2], dp[len(prices)-1][0][1], 0)

class Solution2(object): # Time Limit Exceeded
    def maxProfit(self, prices):
        def onetime(prices):
            minprice, maxprofit = prices[0], 0
            for i in range(1, len(prices)):
                if prices[i] < minprice:
                    minprice = prices[i]
                elif prices[i] - minprice > maxprofit:
                    maxprofit = prices[i] - minprice
            return maxprofit

        try:
            profit1, profit2 = 0, 0
            maxprofit = 0
            for i in range(len(prices)):
                if i == 0 or i == len(prices)-1:
                    totalprofit = onetime(prices)
                else:
                    profit1 = onetime(prices[0:i+1])
                    profit2 = onetime(prices[i:len(prices)])
                    totalprofit = profit1 + profit2

                if totalprofit > maxprofit:
                    maxprofit = totalprofit
        except: maxprofit = 0
        return maxprofit

class Solution3(object):
    def maxProfit(self, prices):
        def onetime(prices):
            minprice, maxprofit = prices[0], 0
            for i in range(1, len(prices)):
                if prices[i] < minprice:
                    minprice = prices[i]
                elif prices[i] - minprice > maxprofit:
                    maxprofit = prices[i] - minprice
            return maxprofit

        # try:
            profit1 = onetime(prices)
            profit2 = onetime()

class Solution4(object): # 没看懂！！
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, total_max_profit = float('inf'), 0
        # 记录顺序区间内每个坐标对应的利润最大值
        first_profit = [0]*len(prices)
        # 从左至右比遍历，获取顺序区间内一次交易利润的最大值
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i]-min_price)
            first_profit[i] = total_max_profit
        max_price, max_profit = float('-inf'), 0
        # 从右至左遍历，获取逆序区间内一次交易利润的最大值，两者相加得到两次利润的最大值
        for i in range(len(prices)-1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price-prices[i])
            total_max_profit = max(total_max_profit, max_profit+first_profit[i-1])
        return total_max_profit

class Solution5(object): # DP
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[3,3,5,0,0,3,1,4]))