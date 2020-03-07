# -*- coding: UTF-8 -*-

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
'''

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # print(nums[:-1])
        if not nums: return 0
        n = len(nums)
        if n <= 2: return max(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[n-1] = nums[n-1]
        dp2[n-2] = max(nums[n-2], nums[n-1])
        for i in range(2, n-1):
            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])
        for i in range(n-3, 0, -1):
            dp2[i] = max(nums[i] + dp2[i + 2], dp2[i + 1])
        return max(max(dp1), max(dp2))

if __name__ == '__main__':
    print(Solution().rob(nums=[6,6,4,8,4,3,3,10]))