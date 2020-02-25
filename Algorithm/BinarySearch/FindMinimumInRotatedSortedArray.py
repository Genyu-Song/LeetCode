# -*- coding: UTF-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = float('inf')
        for i in nums:
            if i < min: min = i
        return min

class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[0]
        while left < right:
            if right - left == 1: break
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[left]

class Solution3:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

'''
小技巧:
一般是这样,
当while left < right是循环外输出
当while left <= right是循环里输出
'''

if __name__ == '__main__':
    print(Solution3().findMin(nums=[4,5,6,7,0,1,2]))