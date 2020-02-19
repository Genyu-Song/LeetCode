# -*- coding: UTF-8 -*-

'''
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.
'''

class Solution: # Greedy Algorithm #1
    def findMinArrowShots(self, points):
        try:
            points.sort(key=lambda x:x[1])
            start, end = points[0]
            arrow = 1
            for l, r in points[1:]:
                if l > end:
                    arrow += 1
                    start, end = l, r
                else:
                    start = l
        except:
            arrow = 0
        return arrow

class Solution2: # Greedy Algorithm #2
    def findMinArrowShots(self, points):
        try:
            points.sort(key=lambda x:x[0], reverse=True)
            start, end = points[0]
            arrow = 1
            for l, r in points[1:]:
               if r < start:
                   arrow += 1
                   start, end = l, r
               else:
                   end = r
        except:
            arrow = 0
        return arrow

if __name__ == '__main__':
    print(Solution2().findMinArrowShots(points=[[1,2],[2,3],[3,4],[4,5]]))