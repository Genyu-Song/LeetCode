# -*- coding: UTF-8 -*-

'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        # dp = [1 for _ in range(N)]
        for i in range(1, N):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution2: # dp + BinarySearch
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        tails = [nums[0]]
        for i in range(1, len(nums)):
            j, flag = 0, False
            while j < len(tails) and flag == False:
                if nums[i] <= tails[j]:
                    tails[j] = nums[i]
                    flag = True
                j += 1
            if flag == False:
                tails.append(nums[i])
        return len(tails)



if __name__ == '__main__':
    print(Solution2().lengthOfLIS(nums=[2,2]))