# -*- coding: UTF-8 -*-

'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
'''

from typing import List
class Solution: # O(NlogN) dp + bs
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 先按第一项元素排序！
        pairs.sort(key=lambda x: x[0])
        tails = [pairs[0]]
        for first, second in pairs:
            for j in range(len(tails)):
                if first > tails[-1][1]:
                    tails.append([first, second])
                    continue
                if second < tails[j][1]:
                    tails[j] = [first, second]
        return len(tails)

class Solution2(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

class Solution(object): # 贪心算法
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x:x[1])
        cur = float('-inf')
        count = 0
        for st, nd in pairs:
            if st > cur:
                count += 1
                cur = nd
        return count

if __name__ == '__main__':
    print(Solution2().findLongestChain(pairs=[[4,5],[2,3],[1,4]]))
