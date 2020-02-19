# -*- coding: UTF-8 -*-

'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        first_ind = last_ind = 0
        res = []
        for i in range(len(S)):
            tempo_ind = length - S[::-1].find(S[i]) - 1
            if tempo_ind >= last_ind:
                last_ind = tempo_ind
            if i == last_ind:
                res.append(last_ind - first_ind + 1)
                first_ind = i + 1
        return res

class Solution2:
    def partitionLabels(self, S):
        t = {}
        for i, c in enumerate(S):
            if c not in t:
                t[c] = (i, i)
            else:
                t[c] = (t[c][0], i)
        t = sorted(t.values(), key=lambda x: x[0])
        re = []
        while t:
            start, end = t.pop(0)
            while t and t[0][0] < end:
                _ , newend = t.pop(0)
                end = max(end, newend)
            re.append(end-start+1)
        return re

if __name__ == '__main__':
    print(Solution2().partitionLabels(S="ababcbacadefegdehijhklij"))