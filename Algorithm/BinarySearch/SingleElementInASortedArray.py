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

class Solution2(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        dict = [[key, value] for key, value in dict.items()]
        dict.sort(key=lambda x:x[1])
        return dict[0][0]

class Solution3(object): # TODO：二分法找单项数
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if m == r or m == l:
                return nums[m]
            if nums[m] == nums[m+1]:
                if (m-l) % 2 != 0:
                    r = m - 1
                else:
                    l = m + 2
            elif nums[m] == nums[m-1]:
                if (m-1-l) % 2 != 0:
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]

if __name__ == '__main__':
    print(Solution3().singleNonDuplicate(nums=[1,1,2]))
