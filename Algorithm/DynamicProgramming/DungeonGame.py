# -*- coding: UTF-8 -*-

'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
'''

from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if len(dungeon) == 1 and len(dungeon[0]) == 1: return 1 if dungeon[0][0] >=0 else 1 - dungeon[0][0]

        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        if dungeon[-1][-1] <= 0:
            dp[-1][-1] = 1 - dungeon[-1][-1]
        else:
            dp[-1][-1] = 1

        for j in range(n-2, -1, -1):
            if dungeon[m-1][j] <= 0:
                dp[m-1][j] = dp[m-1][j + 1] - dungeon[m-1][j]
            else:
                if dp[m-1][j + 1] - dungeon[m-1][j] >= 1:
                    dp[m-1][j] = dp[m-1][j + 1] - dungeon[m-1][j]
                else:
                    dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            if dungeon[i][n-1] <= 0:
                dp[i][n-1] = dp[i + 1][n-1] - dungeon[i][n-1]
            else:
                if dp[i + 1][n-1] - dungeon[i][n-1] >= 1:
                    dp[i][n-1] = dp[i + 1][n-1] - dungeon[i][n-1]
                else:
                    dp[i][n-1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if dungeon[i][j] <= 0:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                else:
                    dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]

class Solution: # 简化代码
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [[0] * col for _ in range(row)]
        # 初始化 右下角最少血量
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        # 行
        for i in range(col - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])
        # 列
        for i in range(row - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])
        #print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]


if __name__ == '__main__':
    print(Solution().calculateMinimumHP(dungeon=[[-2,-3,3],
                                                 [-5,-10,1],
                                                 [10,30,-5]]))