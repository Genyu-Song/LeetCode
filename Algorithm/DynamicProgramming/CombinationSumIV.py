# -*- coding: UTF-8 -*-

'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=False)
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for d in nums:
                if i - d < 0:
                    break
                dp[i] += dp[i - d]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().combinationSum4(nums=[1,2,5], target=11))