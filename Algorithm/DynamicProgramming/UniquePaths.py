# -*- coding: UTF-8 -*-

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TODO: C((m-1+n-1), (m-1)) 或者 C((m-1+n-1), (n-1)) 解释：在一共m+n-2次移动中，随机挑选几步进行横向或竖向的移动
        return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))

class Solution2: # dp
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0: dp[i][j] = 1
                elif j == 0: dp[i][j] = 1
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(m=7, n=3))