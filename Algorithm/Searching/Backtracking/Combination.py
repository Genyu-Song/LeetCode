# -*- coding: UTF-8 -*-

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []

        def backtrack(path, index):
            if len(path) == k:
                output.append(path[:])
            for i in range(index, n):
                path.append(i+1)
                backtrack(path, i+1)
                path.pop()

        backtrack([], index=0)
        return output


class Solution2: # 字典序 (二进制排序) 组合
    def combine(self, n, k):
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]

        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output


if __name__ == '__main__':
    print(Solution().combine(n=4, k=2))