# -*- coding: UTF-8 -*-

'''
# 474
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
'''

from typing import List
from collections import defaultdict
class Solution: # 三维dp, 理解起来和[11, 5, 5, 1]填满一半包一个意思。
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(1 + len(strs))]

        for i in range(1, len(strs)+1):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i-1][j][k]
                    zeros = strs[i-1].count('0')
                    ones = strs[i-1].count('1')
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i-1][j][k],
                                          1 + dp[i-1][j - zeros][k - ones])
        return dp[-1][-1][-1]

class Solution2: # 二维dp，从后往前填！否则更新[j][k]所需要的旧[j][k]会被覆盖！
                 # 就本身未降维的情况，更新[i]行时也是可以从后向前填的，因为它不取决于自身行的数据
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, len(strs)+1):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    zeros = strs[i-1].count('0')
                    ones = strs[i-1].count('1')
                    if j >= zeros and k >= ones:
                        dp[j][k] = max(dp[j][k],
                                       1 + dp[j - zeros][k - ones])
        return dp[-1][-1]

if __name__ == '__main__':
    print(Solution2().findMaxForm(strs=["00","000"],
                                 m=1,
                                 n=10))