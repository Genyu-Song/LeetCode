# -*- coding: UTF-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        try:
            for i in range(0, len(flowerbed)):
                if i == 0:
                    if flowerbed[i+1] == 0 and flowerbed[i] != 1:
                        flowerbed[i] = 1
                        count += 1
                if i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i] != 1:
                        flowerbed[i] = 1
                        count += 1
                if i != 0 and i != len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] != 1:
                        flowerbed[i] = 1
                        count += 1
                if count >= n:
                    return True
        except:
            if len(flowerbed) == 0:
                return False
            else:
                if flowerbed[0] == 0:
                    count += 1
                if count >= n:
                    return True
        return False

class Solution2(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n > (len(flowerbed) - sum(flowerbed)) // 2 + 1:
            return False

        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False

if __name__ == '__main__':
    print(Solution2().canPlaceFlowers(flowerbed=[0], n=1))