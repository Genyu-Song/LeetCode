# -*- coding: UTF-8 -*-

'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)-1
        while start != end:
            twosum = numbers[start] + numbers[end]
            if twosum < target:
                start += 1
            elif twosum == target:
                break
            elif twosum > target:
                end -= 1
        return [start+1, end+1]

if __name__ == '__main__':
    print(Solution().twoSum(numbers = [1, 3, 5, 6, 9], target=11))