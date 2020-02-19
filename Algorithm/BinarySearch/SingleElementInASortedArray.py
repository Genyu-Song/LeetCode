# -*- coding: UTF-8 -*-

'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one

element which appears exactly once. Find this single element that appears only once.
'''

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            dict.
