# -*- coding: UTF-8 -*-

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         known_result = {}
#         known_result[target] = []
#         search_list = [target]
#         res = []
#
#         def bfs():
#             while search_list:
#                 residue = search_list.pop()
#                 for i in candidates:
#                     if residue - i == 0:
#                         res.append(known_result[residue - i].append(i))
#                     if residue - i not in known_result:
#                         a = known_result[residue]
#                         known_result[residue - i] = a.append(i)
#                         search_list.append(residue-i)
#         bfs()
#         return res

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return
        candidates = sorted(candidates)
        output = []

        def dfs(residue, path, nums):
            for index, val in enumerate(nums):
                if residue - val > 0:
                    path.append(val)
                    dfs(residue-val, path, nums[index:])
                elif residue - val == 0:
                    path.append(val)
                    if sorted(path) not in output:
                        output.append(sorted(path[:]))
                    path.pop()
                elif residue - val < 0:
                    if path: path.pop()
                    return
            if path: path.pop()

        dfs(target, [], candidates)
        return output

class Solution2(object): # 更易理解
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return
        candidates = sorted(candidates)
        output = []

        def dfs(target, path, start):
            if target == 0:
                # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
                # 或者使用 path.copy()
                output.append(path[:])
                return

            for index in range(start, len(candidates)):
                residue = target - candidates[index]
                if residue < 0:
                    break
                else:
                    path.append(candidates[index])
                    dfs(residue, path, index)
                    path.pop()
        dfs(target, [], 0)
        return output

class Solution3(object): # 更易理解（加法版本）
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return

        candidates = sorted(candidates)
        target = target
        output = []

        def __dfs(last_sum, begin, path):
            if last_sum == target:
                output.append(path[:])
                return

            for index in range(begin, len(candidates)):
                tempo_sum = last_sum + candidates[index]
                if tempo_sum > target:
                    break
                else:
                    path.append(candidates[index])
                    __dfs(tempo_sum, index, path)
                    path.pop()

        __dfs(0, 0, [])
        return output

if __name__ == '__main__':
    print(Solution3().combinationSum(candidates=[8,7,4,3], target=11))