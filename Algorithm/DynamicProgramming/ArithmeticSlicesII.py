# -*- coding：UTF-8 -*-

'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.
'''

from typing import *
from collections import defaultdict
class Solution: # TODO: 复习！
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n=len(A)
        maps=[defaultdict(lambda :0) for _ in range(n)]
        total=0
        for i in range(1,n):
            for j in range(i):
                add_val=(maps[j][A[i]-A[j]]+1)
                maps[i][A[i]-A[j]]+=add_val
                total+=add_val-1
        return total

if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices(A=[1,2,3,4,5,6]))