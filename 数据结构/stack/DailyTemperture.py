# -*- coding: UTF-8 -*-

'''
#739. 每日温度

根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''

from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            if not stack:
                stack.insert(0, i)
            else:
                while True:
                    if T[i] > T[stack[0]]:
                        tmp = stack.pop(0)
                        res[tmp] = i - tmp
                        if not stack:
                            stack.insert(0, i)
                            break
                    else:
                        stack.insert(0, i)
                        break
        return res

class Solution2(object):
    def dailyTemperatures(self, T):
        stack, output = [], [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                output[stack.pop()] = i - stack[-1]
            stack.append(i)
        return output

if __name__ == '__main__':
    print(Solution().dailyTemperatures(T=[73,74,75,71,69,72,76,73]))