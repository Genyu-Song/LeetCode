# -*- coding: UTF-8 -*-

'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

# https://leetcode-cn.com/problems/subsets-ii/solution/pai-xu-hui-su-zhu-xing-jie-shi-python3-by-zhu_shi_/
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        nums = sorted(nums)
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                pre = [curr + [nums[index]] for curr in output]
            else:
                pre = [curr + [nums[index]] for curr in output]
            output += pre

        res = []
        for instance in output:
            if instance not in res:
                res.append(instance)
        return res

class Solution2(object): # 带剪枝版本
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums = sorted(nums)
        def __dfs(path, begin):
            if path not in output:
                output.append(path[:])
            for index in range(begin, len(nums)):
                if (path == [] and nums[index] == nums[index - 1]): # TODO: 注意剪枝条件！
                    continue
                path.append(nums[index])
                __dfs(path, index+1)
                path.pop()
        __dfs([], 0)
        return output

if __name__ == '__main__':
    print(Solution().subsetsWithDup(nums=[1,2,1]))