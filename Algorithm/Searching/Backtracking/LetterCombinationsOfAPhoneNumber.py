# -*- coding: UTF8 -*-

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution(object): # DFS
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '1' in list(digits): return False
        if len(digits) == 0: return []
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        table = []
        res = []
        for i in list(digits):
            table.append(dic[i])

        def dfs(i, j, str):
            str.append(table[j][i])
            if j + 1 < len(table):
                for x in range(len(table[j+1])):
                    dfs(x, j + 1, str)
                del str[-1]
            else:
                res.append(''.join(str))
                del str[-1]


        for i in range(len(table[0])):
            str = []
            dfs(i, 0, str)

        return res


class Solution2: # 官方优化版本 TODO: 简化Solution1
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

if __name__ == '__main__':
    print(Solution().letterCombinations(digits='999'))