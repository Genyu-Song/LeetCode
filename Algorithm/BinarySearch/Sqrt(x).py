# -*- coding: UTF-8 -*-

'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def binarysearch(goal, start, end):
            m = start + (end - start) // 2
            if round(m ** 2) > goal:
                if round((m-1)**2) < goal:
                    return m-1
                return binarysearch(goal, start, m-1)
            elif round(m ** 2) < goal:
                if round((m+1)**2) > goal:
                    return m
                return binarysearch(goal, m+1, end)
            if round(m ** 2) == goal:
                return m
        if x < 2: return x
        return binarysearch(x, 0, x)

if __name__ == '__main__':
    print(Solution().mySqrt(2147395600))