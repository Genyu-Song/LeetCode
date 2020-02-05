# -*- coding: UTF-8 -*-

'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
'''

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        flag = False
        list = [i for i in range(0, int(round(math.sqrt(c))))]
        start, end = 0, len(list)
        while start <= end:
            tempo = start**2 + end**2
            if tempo > c:
                end -= 1
            elif tempo < c:
                start +=1
            elif tempo == c:
                flag = True
                break
        return flag

if __name__ == '__main__':
    print(Solution().judgeSquareSum(1))