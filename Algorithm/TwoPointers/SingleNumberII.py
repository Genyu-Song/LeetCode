# -*- coding: UTF-8 -*-

'''
137. Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.
'''

import time

class Solution(object):
    def method1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((3 * sum(set(nums)) - sum(nums)) / 2)

    def method2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = []
        list2 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
            else:
                list2.append(i)
        for j in set(list2):
            list1.remove(j)
        return list1.pop()

    def method3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        TODO:
        ~: It returns the one’s complement of a number’s binary.
        ????
        """
        one, two = 0, 0
        for x in nums:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one



if __name__ == '__main__':
    starttime = time.time()
    print(Solution().method1(nums = [0, 1, 0, 1, 0, 1, 99]))
    print(1000 * (time.time() - starttime))

    starttime = time.time()
    print(Solution().method2(nums = [0, 1, 0, 1, 0, 1, 99]))
    print(1000 * (time.time() - starttime))

    starttime = time.time()
    print(Solution().method3(nums = [0, 1, 0, 1, 0, 1, 99]))
    print(1000 * (time.time() - starttime))