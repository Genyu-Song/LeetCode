# -*- coding: UTF-8 -*-

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
'''

class Solution(object): # TODO: 复习！
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        output = []

        def __dfs(path, str):
            if not str:
                output.append(path)
            for i in range(1, len(str) + 1):
                suffix = str[:i]
                if suffix == suffix[::-1]:
                    __dfs(path + [suffix], str[i:])

        __dfs([], s)
        return output

class Solution2:
    '''
    作者：li-li-li
    链接：https://leetcode-cn.com/problems/palindrome-partitioning/solution/dong-tai-gui-hua-zi-dian-hashmap-by-li-li-li/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    def partition(self, s: str):
        # 动态规划
        # dp[i][j]表示第i到第j个字符是否是回文串

        if len(s) == 0:
            return []

        hashmap = {}
        dp = [[False] * len(s) for _ in range(len(s))]

        for end in range(len(s)):
            r = []
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    if start == 0:
                        r.append([s[start:end + 1]])
                    else:
                        # 如果s[start:end + 1]是回文子串，那么s[:end + 1]的分割形式可以是s[:start]的分割形式+s[start:end + 1]
                        # hashmap[s[:start]]就保存着s[:start]的分割形式
                        for temp in hashmap[s[:start]]:
                            r.append(temp + [s[start:end + 1]])
            hashmap[s[:end + 1]] = r
        return hashmap[s]

from coll
if __name__ == '__main__':
    print(Solution().partition(s='aaba'))