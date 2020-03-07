# -*- coding: UTF-8 -*-

'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []

        def __dfs(target, path, begin):
            # print(target, path, begin)
            if target == 0:
                output.append(path[:])
                return
            for i in range(begin, 10):
                residue = target - i
                if residue < 0:
                    break
                else:
                    path.append(i)
                    __dfs(residue, path, i+1)
                    path.pop()

        __dfs(n, [], 1)

        res = []
        for instance in output:
            if len(instance) == k:
                res.append(instance)
        return res

if __name__ == '__main__':
    print(Solution().combinationSum3(k=3, n=7))