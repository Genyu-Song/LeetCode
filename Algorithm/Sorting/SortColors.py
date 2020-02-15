# -*- coding: UTF-8 -*-

'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        TODO: ??
        """
        map_dict = {}
        for i in nums:
            map_dict[i] = map_dict.get(i, 0) + 1
        max_times = max(map_dict.values())
        res = []
        for color in range(max(set(nums))+1):
            count = 0
            while count < map_dict[color]:
                res.append(color)
                count += 1
        return res

import random

class Solution2:
    def sortColors(self, nums):
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        pivot = 1
        lt, gt = 0, len(nums)-1
        pointer = 0
        while pointer <= gt:
            if nums[pointer] < pivot:
                swap(nums, pointer, lt)
                lt += 1
                pointer += 1
            elif nums[pointer] > pivot:
                swap(nums, gt, pointer)
                gt -= 1
            elif nums[pointer] == pivot:
                pointer += 1；
        return nums

if __name__ == '__main__':
    print(Solution2().sortColors(nums=[2,0,2,1,1,0,1,0]))