# -*- coding: UTF-8 -*-

'''
Given a collection of distinct integers, return all possible permutations.
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return nums
        result = []
        N = len(nums)
        visited = [False for _ in range(N)]
        def backtrack(path):
            if len(path) == N:
                '''
                path这个变量所指向的对象在递归的过程中只有一份，深度优先遍历完成以后，
                因为回到了根结点（因为我们之前说了，从深层结点回到浅层结点的时候，需要
                撤销之前的选择），因此path这个变量回到根结点以后都为空。
                所以用result.append(path[:])代替result.append(path)就可以了
                '''
                result.append(path[:])
                return
            for i in range(N):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    visited[i] = False
                    path.pop()
        backtrack([])
        return result

import itertools
class Solution2(object):
    def permute(self, nums):
        return list(itertools.permutations(nums))

if __name__ == '__main__':
    print(Solution2().permute(nums=[1,2,3]))