# -*- coding: UTF-8 -*-

'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
'''

class Solution(object):
    def method1(self, s):
        """
        :type s: str
        :rtype: bool

        TODO:
        del str[index]
        """
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: return True
        return s == s[::-1]

    def method2(self, s):
        """
        :type s: str
        :rtype: bool

        TODO:
        del str[index]
        Two loop to make sure only one character will be delete.
        """
        def validPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return validPalindrome(s, left, right-1) or validPalindrome(s, left+1, right)
            left, right = left+1, right-1
        return True



if __name__ == '__main__':
    print(Solution().method2(s="abcsbdewbfsdfa"))