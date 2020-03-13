# -*- coding: UTF-8 -*-

'''
#650
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
'''

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1) # dp[n]指到n时，需要最少多少个操作
        dp[1] = 0
        for i in range(2, n+1):
            min_v = float('inf')
            for j in range(1, i):
                if i % j == 0:
                    min_v = min(min_v, dp[j] + i/j)
                j += 1
            dp[i] = min_v

        return int(dp[n])

if __name__ == '__main__':
    print(Solution().minSteps(n=3))