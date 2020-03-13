# -*- coding: UTF-8 -*-

'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k
non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''

from typing import List
class Solution: # 迭代
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_all = sum(nums)
        if sum_all % k != 0: return False

        nums.sort(reverse=True)
        N = len(nums)
        target = sum_all // k

        if nums[0] > target: return False

        def search(groups=[0]*k):
            if not nums: return True
            val = nums.pop(0)
            for ind, group in enumerate(groups):
                if groups[ind] + val <= target:
                    groups[ind] += val
                    if search(groups):
                        return True
                    groups[ind] -= val
                # if groups[i] == 0: break
            nums.append(val)
            return False

        return search()

class Solution: # dp
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ??


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets(nums=[7,2,6,3,5,4], k=3))