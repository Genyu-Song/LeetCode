# -*- coding: UTF-8 -*-

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
'''

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for _ in range(len(nums) + 1)]
        for ind in range(len(nums)):
            self.dp[ind+1] = self.dp[ind] + nums[ind]
        a = 1

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(0, 2)
    param_2 = obj.sumRange(2, 5)
    print(param_1, param_2)
