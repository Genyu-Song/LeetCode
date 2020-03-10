# -*- coding: UTF-8 -*-

'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
'''

class Solution: # 递归
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        def dp(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            elif s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        return dp(0, len(s)-1)

class Solution2: # dp
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        s_r = s[::-1]
        dp = [[0] * (N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if s[i-1] == s_r[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

class Solution3: # dp
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][N-1]

if __name__ == '__main__':
    print(Solution3().longestPalindromeSubseq(s="abca"))