# -*- coding: UTF-8 -*-

'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those
integers. Return the maximum product you can get.
'''

import math
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n
        residue = n % 3
        amount = (n - residue) / 3
        output = math.pow(3, amount)
        if residue == 2:
            output *= 2
        if residue == 1:
            output /= 3
            output *= 4
        return int(output)

if __name__ == '__main__':
    print(Solution().integerBreak(n=10))