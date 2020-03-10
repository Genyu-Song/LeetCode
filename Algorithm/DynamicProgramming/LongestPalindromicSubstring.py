# -*- coding: UTF-8 -*-

'''
#5
Similiar to #1143 # 516
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

class Solution: # 暴力搜索
    def isvaild(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N < 2: return s
        max_len = 1
        res = s[0]
        for i in range(N-1):
            for j in range(i, N):
                if j - i + 1 > max_len and self.isvaild(s, i, j):
                    res = s[i:j+1]
                    max_len = j - i + 1
        return res

class Solution2: # dp
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N < 2: return s
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
        max_len = 1
        start = 0
        end = 0
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    if j - i + 1 < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    end = j
        return s[start: end+1]

# 非连续字符最长回文字串
class Solution_other_question:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        s = list(s)
        N = len(s)
        dp = [[[0, ''] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = [1, s[i]]
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    temp_s = dp[i+1][j-1][1]
                    dp[i][j] = [2 + dp[i+1][j-1][0],
                                s[i] + temp_s + s[j]]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], key=lambda x:x[0])
        return dp[0][-1][1]

if __name__ == '__main__':
    print(Solution2().longestPalindrome(s="aa"))