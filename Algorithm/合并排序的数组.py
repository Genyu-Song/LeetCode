# -*- coding: UTF-8 -*-

from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        res = []
        i = 0
        j = 0
        while i < m or j < n:
            if i == m:
                res.append(B[j])
                j += 1
            elif j == n:
                res.append(A[i])
                i += 1
            elif A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        A[:] = res
        return A

if __name__ == '__main__':
    print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))