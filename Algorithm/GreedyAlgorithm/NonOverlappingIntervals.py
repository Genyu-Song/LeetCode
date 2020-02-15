# -*- coding: UTF-8 -*-

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

class Solution: # Greedy Algorithm #1
    def eraseOverlapIntervals(self, intervals):
        try:
            intervals.sort(key=lambda x:x[1])
            lt, gt = intervals[0]
            count = 0
            for left, right in intervals[1:]:
                if left < gt:
                    count += 1
                else:
                    gt = right
            return count
        except:
            return 0

class Solution2: # Greedy Algorithm #2
    def eraseOverlapIntervals(self, intervals):
        try:
            intervals.sort(key=lambda x:x[0], reverse=True)
            lt, gt = intervals[0]
            count = 0
            for left, right in intervals[1:]:
                if right > lt:
                    count += 1
                else:
                    lt = left
            return count
        except:
            return 0

class Solution3:
    def eraseOverlapIntervals(self, intervals):
        try:
            intervals.sort(key=lambda x:x[0])
            dp = [[(l, r), 0] for l, r in intervals]
            dp[0][1]= 1
            for j in range(1, len(intervals)):
                flag = False
                i = j - 1
                while i >= 0 and flag == False:
                # for i in range(j-1: -1: -1):
                    if dp[j][0][0] >= dp[i][0][1]:
                        flag = True
                        dp[j][1] = max([numb for numb in dp[0:i+1]], key=lambda x:x[1])[1] + 1
                    else:
                        dp[j][1] = 1
                    i -= 1
            res = len(intervals) - max(dp, key=lambda x:x[1])[1]
        except:
            res = 0
        return res

if __name__ == '__main__':
    print(Solution3().eraseOverlapIntervals(intervals=[[1,2],[1,2],[1,2]]))