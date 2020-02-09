# -*- coding: UTF-8 -*-

'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str

        TODO:
        Be careful of the difference between
        d.sort(key = lambda x: -len(x)) and d.sort(key = lambda x: (-len(x), x))
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
                if i == len(word):
                    return word
        return ""

if __name__ == "__main__":
    print(Solution().findLongestWord(s="bab", d=["ba","ab","a","b"]))