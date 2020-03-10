# -*- coding: UTF-8 -*-

'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k
non-empty subsets whose sums are all equal.
'''

class Solution:
    def canPartitionKSubsets(self, nums, k):
        sum_all = sum(nums)
        if sum_all % k != 0: return False

        nums.sort(reverse=True)
        N = len(nums)
        target = sum_all // k
        if nums[0] > target: return False

        def search(groups):
            if not nums: return True
            val = nums.pop()
            for ind, group in enumerate(groups):
                if group + val <= target:
                    groups[ind] += val
                    if search(groups):
                        return True
                    groups[ind] -= val
                if not group:
                    break
                nums.append(val)
                return False

        return search([0] * k)

if __name__ == '__name__':
    solver = Solution()
    res = solver.canPartitionKSubsets(nums=[4, 2], k=4)
    print(res)