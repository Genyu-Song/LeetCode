# -*- coding：UTF-8 -*-

'''
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''

from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        dp = [0 for _ in range(N - 1)]
        for ind in range(N - 1):
            dp[ind] = A[ind + 1] - A[ind]

        output = 0
        for i in range(N - 2):
            j = i + 1
            flag = False
            while j < N - 1 and flag == False:
                if dp[i] == dp[j]:
                    output += 1
                else:
                    flag = True
                j += 1

        return output

if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices(A=[1,2,3,4]))

