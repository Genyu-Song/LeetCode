# -*- coding: UTF-8 -*-

'''
# 367
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
'''

from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        diff = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        N = len(diff)
        dp = [2 if diff[_] != 0 else 1 for _ in range(N)]
        for i in range(N):
            for j in range(i):
                if diff[i] * diff[j] < 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution2: # Greedy
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1

        start = 0
        symbols = -1
        while start < len(nums) - 1:
            if nums[start+1] - nums[start] > 0:
                symbols = 0 # 0 for positive, 1 for negative
                break
            elif nums[start+1] - nums[start] < 0:
                symbols = 1
                break
            start += 1

        if symbols == -1: return 1

        N = len(nums)
        temp = nums[start+1]
        count = 2

        for i in range(start+1, N):
            if symbols == 0:
                if nums[i] < temp:
                    symbols ^= 1
                    count += 1
            else:
                if nums[i] > temp:
                    symbols ^= 1
                    count += 1
            temp = nums[i]
        return count

if __name__ == '__main__':
    print(Solution2().wiggleMaxLength(nums=[33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]))