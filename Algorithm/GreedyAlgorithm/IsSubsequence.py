# -*- coding: UTF-8 -*-

'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        try:
            count = 0
            t = list(t)
            for letter in s:
                while letter != t[0]:
                    del t[0]
                if letter == t[0]:
                    count += 1
                    del t[0]
                else:
                    return False
            return count == len(s)
        except:
            return False

class Solution2(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        loc = -1
        for c in s:
            loc = t.find(c, loc + 1) # TODO： str.find(str, beg=0, end=len(string))，如果找不到返回-1
            if loc == -1:
                return False
        return True

class Solution3(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(c in list(t) for c in s)

class Solution4(object):
    def isSubsequence(self, s, t):
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == '__main__':
    print(Solution4().isSubsequence(s = "axc", t = "ahxgdc"))