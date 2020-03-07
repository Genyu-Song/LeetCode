# -*- coding: UTF-8 -*-

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return nums
        N = len(nums)
        output = []
        visited = [False for _ in range(N)]
        nums.sort()

        def backtrack(path):
            if len(path) == N:
                if path not in output:
                    output.append(path[:])
            for i in range(N):
                if i > 0 and nums[i-1] == nums[i] and visited[i-1] == False: # TODO: 注意这里的剪枝条件！visited[i-1] == False
                    continue
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    visited[i] = False
                    path.pop()

        backtrack([])
        return output

class Solution2:
    def permuteUnique(self, nums):
        nums.sort() # 数组先排序
        self.res = []
        self.recur(nums, [])
        return self.res

    def recur(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue
            self.recur(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用。

if __name__ == '__main__':
    print(Solution2().permuteUnique(nums=[1,1,2]))