# -*- couding: UTF-8 -*-

'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to
group numbers and operators. The valid operators are +, - and *.
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[1+i:])
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        elif char == '*':
                            res.append(l * r)
        return res


if __name__ == '__main__':
    print(Solution().diffWaysToCompute(input="2-1-1+3"))