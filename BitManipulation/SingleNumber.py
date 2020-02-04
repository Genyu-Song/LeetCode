# -*- coding: UTF-8 -*-

'''
136. Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

import time
import operator
from functools import reduce

class Solution(object):
    def method1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

    def method2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Hash Table: 1. Key   2. Value   3. Hash Func.
                    Map Key to Value by: Hash(Key) => index
                    Hash will tell you exactly where, which index, to start up.
                    If there is chaining, it will kind of go down the list and figure our exactly.

                    Collision - Several value in one index.
                    Chaining - Links from each different value to the index.

        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def method3(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        set() is an unordered collection with no duplicate elements.
        """
        return(2 * sum(set(nums)) - sum(nums))

    def method4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a = a^i
        return a

    def method5(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        reduce的工作过程是 ：在迭代sequence(tuple ，list ，dictionary， string等可迭代物)的过程中，首先把 前两个元素传给 函数参数，
        函数加工后，然后把得到的结果和第三个元素作为两个参数传给函数参数， 函数加工后得到的结果又和第四个元素作为两个参数传给函数参数，依
        次类推。 如果传入了 initial 值， 那么首先传的就不是 sequence 的第一个和第二个元素，而是 initial值和 第一个元素。经过这样的累计
        计算之后合并序列到一个单一返回值
        """
        return(reduce(operator.xor, nums))

if __name__ == '__main__':
    starttime = time.time()
    print(Solution().method1(nums = [1, 3, 1]))
    print(time.time() - starttime)

    starttime = time.time()
    print(Solution().method2(nums = [1, 3, 1]))
    print(time.time() - starttime)

    starttime = time.time()
    print(Solution().method3(nums = [1, 3, 1]))
    print(time.time() - starttime)

    starttime = time.time()
    print(Solution().method4(nums = [1, 3, 1]))
    print(time.time() - starttime)

    starttime = time.time()
    print(Solution().method5(nums = [1, 3, 1]))
    print(time.time() - starttime)