# -*- coding: UTF-8 -*-

'''
#994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''

from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = []
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        depth = 0
        while queue and count > 0:
            depth += 1
            for n in range(len(queue)):
                i, j = queue.pop(0)
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= i + di < R and 0 <= j + dj < C:
                        if grid[i + di][j + dj] == 1:
                            grid[i + di][j + dj] = 2
                            count -= 1
                            queue.append((i + di, j + dj))

        return depth if count == 0 else -1

if __name__ == '__main__':
    print(Solution().orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]]))