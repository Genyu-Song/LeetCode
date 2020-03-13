# -*- coding: UTF-8 -*-

'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[0] * (N2+1) for _ in range(N1+1)]

        for i in range(N1+1):
            dp[i][0] = 0

        for i in range(N2+1):
            dp[0][i] = 0

        for i in range(1, N1+1):
            for j in range(1, N2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return N1 + N2 - 2 * dp[-1][-1]

if __name__ == '__main__':
    print(Solution().minDistance(word1='sea', word2='eat'))