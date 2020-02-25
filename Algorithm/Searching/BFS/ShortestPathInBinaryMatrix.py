# -*- coding: UTF-8 -*-

'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
'''

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        if len(grid) == 0 or grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        direction = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        known_result = {}
        known_result[0, 0] = 1
        search_queue = [[0, 0]]
        i = j = 0
        count = 0
        while True:
            for i, j in search_queue:
                count += 1
                for x, y in direction:
                    if i+x >= 0 and j+y >= 0 and i+x <= N-1 and j+y <= N-1 and grid[j+y][i+x] == 0:
                        if not known_result.__contains__((i+x, j+y)):
                            known_result[i+x, j+y] = known_result[i, j] + 1
                            search_queue.append([i+x, j+y])
                grid[i][j] = 1
            if known_result.__contains__((N-1, N-1)):
                return known_result[N-1, N-1]
            else:
                return -1

if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix(grid=[[0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1],[1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1],[0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1],[0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0],[0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0],[1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1],[0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0],[1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1],[1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0],[0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1],[1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1],[0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0],[1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1],[0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0],[0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0],[0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0],[0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1],[0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0],[1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0],[0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0],[1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1],[1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1],[1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1],[0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1],[0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1],[1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1],[1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0],[1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1],[1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0],[0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0],[0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0],[1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1],[1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],[1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1],[0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1],[1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1],[0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0],[1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0],[0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0],[1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0],[0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0],[1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0],[1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0],[1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1],[1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1],[1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1],[1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1],[0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1],[1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1],[0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1],[0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1],[0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0],[0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1],[0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1],[1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0],[0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0],[1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1],[1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0],[1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1],[0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0],[0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0],[1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0],[1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1],[0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0],[0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0],[0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0],[0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1],[1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1],[0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1],[1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0],[1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0],[0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1],[0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1],[1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0],[1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0],[1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1],[0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1],[1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1],[0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1],[1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0],[0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1],[0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1],[0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1],[0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0],[0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0]]))


