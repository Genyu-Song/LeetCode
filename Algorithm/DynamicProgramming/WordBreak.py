# -*- codind: UTF -*-

'''
#139
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        return dp[-1] 

if __name__ == '__main__':
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))