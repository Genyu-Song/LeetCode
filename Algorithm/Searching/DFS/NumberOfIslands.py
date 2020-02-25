# -*- coding: UTF-8 -*-

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return 0 if len(grid) == 0

        R, C = len(grid)

        def dfs(i, j):
            if 0 <= i < C and 0 <= j < R and grid[j][i] == '1':
                grid[j][i] = 0
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(c, r)
                    count += 1
        return count

if __name__ == '__main__':
    print(Solution().numIslands(grid=[]))