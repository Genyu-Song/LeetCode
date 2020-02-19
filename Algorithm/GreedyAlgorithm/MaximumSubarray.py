# -*- coding: UTF-8 -*-

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        dp = [[] for _ in range(len(nums))]
        dp[0] = float('-inf')
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        res = max(dp)
        return res

class Solution2:
    def maxSubArray(self, nums):
        n = len(nums)
        sum = 0
        maxsum = float('-inf')
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                maxsum = max(maxsum, sum)
        return maxsum

class Solution3:
    def maxSubArray(self, nums):
        if len(nums) == 0: return False
        s_max = nums[0]
        s_min = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            s_max = max(s_max, s-s_min)
            s_min = min(s_min, s)
        return s_max

import sys
class Solution4: # 分治法（https://leetcode-cn.com/problems/maximum-subarray/solution/wu-chong-jie-fa-san-chong-yu-yan-java-javascript-2/）
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)
    def helper(self, nums, l, r):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        sum = 0
        for i in reversed(range(l, mid)):
            sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, sum)
        sum = 0
        for i in range(mid + 1, r + 1):
            sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)

if __name__ == '__main__':
    print(Solution4().maxSubArray(nums=[1, -2]))