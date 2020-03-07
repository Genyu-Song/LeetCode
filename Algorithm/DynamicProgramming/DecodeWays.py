# -*- coding: UTF-8 -*-

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(s)
        if s[0] == '0': return 0
        zeroes_index = [i for i, x in enumerate(s) if x == '0']
        print(zeroes_index)
        # 如果0前面一个数大于2，返回0
        # 如果0前面一个数小于等于2， 去掉这两个数
        count = 0
        for i in zeroes_index:
            if int(s[i-1]) > 2:
                return 0
            elif int(s[i-1]) == -1:
                return 0
            else:
                s[i] = s[i-1] = -1
                count += 1
        for i in range(count):
            s.remove(-1)

        N = len(s)
        count = 0
        dp = [1, 1]
        for i in range(2, N+1):
            if s[i-1] == -1 or s[i-2] == -1:
                continue
            if i < N+1 and int(s[i-2] + s[i-1]) <= 26:
                count += 1
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])

        # return count + 1
        return dp[-1]

class Solution2: # 简化Solution 1
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]

class Solution3:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [1 for _ in range(len(s) + 1)]
        for i in range(1, len(s)):
            if int(s[i] + s[i-1]) <= 26:
                dp[i] = dp[i-1] + path.pop()
                path.append()
            else:
                path = [1]
            # 遇到大于26的重置斐波那契




if __name__ == '__main__':
    print(Solution3().numDecodings(s='13010'))