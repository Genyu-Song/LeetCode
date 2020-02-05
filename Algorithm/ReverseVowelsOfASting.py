# -*- coding: UTF-8 -*-

'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        index = []
        value = []
        n = 0
        s = list(s)

        for i in s:
            if i in vowels:
                index.append(n)
                value.append(i)
            n += 1
        value = value[::-1]

        for ind, val in zip(index, value):
            s[ind] = val

        return ''.join(s)

if __name__ == '__main__':
    print(Solution().reverseVowels(s = 'hello'))