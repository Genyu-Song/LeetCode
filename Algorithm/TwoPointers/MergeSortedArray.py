# -*- coding: UTF-8 -*-

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        s = nums1[:m] + nums2
        s = sorted(s)
        return s

if __name__ == '__main__':
    print(Solution().merge(nums1=[1,2,3,9,0,0], m=4, nums2=[2,5], n=2))