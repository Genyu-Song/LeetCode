# -*- coding: UTF-8 -*-

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []
        def __dfs(path, begin):
            if path not in output:
                output.append(path[:])
            for index in range(begin, len(nums)):
                path.append(nums[index])
                __dfs(path, index+1)
                path.pop()

        __dfs([], 0)
        return output

from typing import List
class Solution2: # TODO: List的加法！
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output] # [[1]+[2]] = [[1, 2]]

        return output

if __name__ == '__main__':
    print(Solution().subsets(nums=[1,2,3]))