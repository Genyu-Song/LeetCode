# -*- coding: UTF-8 -*-

'''
754. 到达终点数字
在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

示例 1:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
'''

# from collections import defaultdict
class Solution:
    def reachNumber(self, target: int) -> int:
        queue = []
        queue.append(0)
        count = 0
        while queue:
            count += 1
            N = len(queue)
            n = 0
            while n < N:
                tmp = queue.pop(0)
                if tmp + count == target:
                    return count
                else:
                    queue.append(tmp + count)
                if tmp - count == target:
                    return co unt
                else:
                    queue.append(tmp - count)
                n += 1

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        tmp_sum = 0
        n = 0
        while tmp_sum < target or (tmp_sum - target) % 2 != 0:
            n += 1
            tmp_sum += n
        return n

if __name__ == '__main__':
    print(Solution().reachNumber(target=2))