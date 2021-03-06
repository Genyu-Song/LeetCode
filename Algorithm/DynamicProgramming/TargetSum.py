# -*- coding: UTF-8 -*-

'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''

from typing import List
class Solution: # dfs 递归
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort(reverse=True)
        N = len(nums)
        count = 0

        def dfs(tempo_res=0, i=0):
            if i == N and tempo_res == S:
                nonlocal count
                count += 1
            if i < N:
                dfs(tempo_res + nums[i], i+1)
                dfs(tempo_res - nums[i], i+1)
        dfs()
        return count

class Solutionx:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d: # 搜索周围节点
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i],i + 1, d)
            return d.get((cur, i), int(cur == S))
        return dfs(0, 0, d)

class Solution2: # dp
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if S > 1000: return 0
        N = len(nums)
        sum_all = sum(nums)
        if sum_all < S: return 0
        dp = [[0 for _ in range(2*sum_all+3)] for _ in range(N)]

        dp[0][sum_all + 1 + nums[0]] += 1
        dp[0][sum_all + 1 - nums[0]] += 1

        for i in range(1, N):
            for j in range(1, 2*sum_all+2):
                if j + nums[i] - sum_all - 1 > sum_all:
                    dp[i][j] = dp[i - 1][j - nums[i]]
                elif j - nums[i] - sum_all - 1 < -sum_all:
                    dp[i][j] = dp[i - 1][j + nums[i]]
                else:
                    dp[i][j] = dp[i-1][j+nums[i]] + dp[i-1][j-nums[i]]

        return dp[-1][S+sum_all+1]

class Solution3:
    # 二维数组版本
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        import collections
        total = sum(nums)
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        # 初始值 0表示第一个元素
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        for i in range(1, len(nums)):
            num = nums[i]
            for sm in range(-total, total+1, 1):
                val = dp[i-1].get(sm+num, 0) + dp[i-1].get(sm-num, 0)
                if val != 0:
                    dp[i][sm] = val
        return dp[-1][S]  # 返回所有元素组合的题解数量


class Solutionxx:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}

        def dfs(nums=nums, target=0):
            if (len(nums), target) in memo:
                return memo[(len(nums), target)]

            if not nums:
                if target == S:
                    return 1
                else:
                    return 0

            res = dfs(nums[1:], target + nums[0]) + dfs(nums[1:], target - nums[0])
            memo[(len(nums), target)] = res
            return res

        return dfs()


if __name__ == '__main__':
    print(Solutionxx().findTargetSumWays(nums=[1, 1, 1, 1, 1],
                                        S=3))