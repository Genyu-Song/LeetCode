# -*- coding: UTF-8 -*-

'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
'''

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.insert(0, float('-inf'))
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i+1]:
                if nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                    count += 1
                else:
                    nums[i] = nums[i+1]
                    count += 1
            if count == 2:
                 return False
        return True


if __name__ == '__main__':
    print(Solution().checkPossibility(nums=[4,3,3,2,4]))