# -*- coding: UTF-8 -*-

'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
'''

from typing import List
import time

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_all = sum(nums)
        def dfs(begin, sum1, sum2):
            if sum1 == sum2:
                return True
            for i in range(begin+1, len(nums)):
                sum1 += nums[i]
                sum2 -= nums[i]
                if sum1 <= sum_all // 2:
                    if dfs(i, sum1, sum2):
                        return True
                sum1 -= nums[i]
                sum2 += nums[i]
            return False

        for ind in range(len(nums)):
            return dfs(0, sum1=nums[ind], sum2=sum(nums)-nums[ind])

class Solution2:
    # 转换位0-1背包问题
    # 某个元素选或者不选，可以装满容量为target//2的背包
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        N = len(nums)
        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(N)]

        for i in range(N):
            dp[i][0] = True

        for j in range(target+1):
            if nums[0] == j:
                dp[0][j] = True
                break

        for i in range(1, N):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[N-1][-1]

class Solution3:
    # 转换位0-1背包问题
    # 某个元素选或者不选，可以装满容量为target//2的背包
    # 用一维dp，压缩存储空间
    def canPartition(self, nums: List[int]) -> bool:
        sum_all = sum(nums)
        if sum_all % 2: return False

        N = len(nums)
        target = sum_all // 2
        dp = [False for i in range(target + 1)]

        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True

        # 注意 j 要逆序处理！
        for i in range(1, N):
            for j in range(target, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i]]

        return dp[-1]

if __name__ == '__main__':
    start = time.time()
    print(Solution3().canPartition(nums=[1, 2, 5]))
    print(time.time() - start)
