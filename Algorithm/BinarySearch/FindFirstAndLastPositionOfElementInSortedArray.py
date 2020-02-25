# -*- coding: UTF-8 -*-

'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            for i in range(len(nums)):
                if nums[i] == target:
                    start = i
                    break
            for j in range(i+1, len(nums)):
                if nums[j] != target:
                    end = j-1
                    return [start, end]
            return [start, len(nums)-1]
        except:
            return [-1,-1]

class Solution2:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]
'''
for ...: else:..., 如果执行了for循环里面的break语句，则else内的语句不执行。
'''

#TODO: 二分法详解：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/

class Solution3(object): # TODO: Important
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findleftboundary(nums, target, left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if left == len(nums):
                return -1
            return left if nums[left] == target else -1

        def findrightboundary(nums, target, left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if right == 0:
                return -1
            return left - 1 if nums[left - 1] == target else -1

        return [findleftboundary(nums, target, 0, len(nums)), findrightboundary(nums, target, 0, len(nums))]


class Solution4: # Better syntax than Solution 3
    def searchRange(self, nums, target):
        left_index = self.twof_left(nums, target)
        right_index = self.twof_right(nums, target)
        return [left_index, right_index]

    def twof_left(self, nums, target):
        if not nums: return -1
        right = len(nums)
        left = 0
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
        if left == len(nums): return -1
        return left if nums[left] == target else -1

    def twof_right(self, nums, target):
        if not nums: return -1
        right = len(nums)
        left = 0
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
        if right == 0: return -1
        return right - 1 if nums[right - 1] == target else -1

if __name__ == "__main__":
    print(Solution7().searchRange(nums = [], target = 2))