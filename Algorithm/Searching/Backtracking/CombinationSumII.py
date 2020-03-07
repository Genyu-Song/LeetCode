# -*- coding: UTF-8 -*-

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return
        output = []
        candidates.sort()

        def __dfs(last_difference, path, begin):
            if last_difference == 0:
                if path not in output:
                    output.append(path[:])
                return
            else:
                for index in range(begin, len(candidates)):
                    residue = last_difference - candidates[index]
                    if residue < 0:
                        break
                    else:
                        path.append(candidates[index])
                        __dfs(residue, path, index+1)
                        path.pop()

        __dfs(target, [], 0)
        return output

if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[10,1,2,7,6,1,5], target=8))