# -*- coding: UTF-8 -*-

'''
# 1143
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
'''

class Solution: # TODO: 暴力递归法
    def longestCommonSubsequence(self, text1, text2):
        def dp(i, j):
            # 空串的 base case
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                # 这边找到一个 lcs 的元素，继续往前找
                return dp(i - 1, j - 1) + 1
            else:
                # 谁能让 lcs 最长，就听谁的
                return max(dp(i - 1, j), dp(i, j - 1))

        # i 和 j 初始化为最后一个索引
        return dp(len(text1) - 1, len(text2) - 1)

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)
        dp = [[0] * (N1+1)] * (N2+1) # TODO: 注意dp和dp2的区别
        dp2 = [[0] * (N1+1) for _ in range(N2+1)]
        for i in range(1, N2+1):
            for j in range(1, N1+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    dp2[i][j] = dp2[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    dp2[i][j] = max(dp2[i-1][j], dp2[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution2().longestCommonSubsequence(text1="bsbininm", text2="jmjkbkjkv"))