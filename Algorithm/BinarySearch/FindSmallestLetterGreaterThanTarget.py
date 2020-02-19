# -*- coding: UTF-* -*-

'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]: return letters[0]
        letters = sorted(list(set(letters)))
        l, r = 0, len(letters)-1
        while l <= r:
            m = l + (r - l) // 2
            if letters[m] < target:
                l = m + 1
            elif letters[m] > target:
                r = m - 1
            elif letters[m] == target:
                return letters[m+1]
        return letters[r+1]

class Solution2:
    def nextGreatestLetter(self, letters, target):
        if target >= letters[-1]: return letters[0]
        letters = sorted(list(set(letters)))
        for c in letters:
            if c > target:
                return c

# TODO： index == bisect.bisect(list, target)
import bisect
class Solution3(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

if __name__ == '__main__':
    print(Solution3().nextGreatestLetter(letters=['c','f','j'], target="z"))