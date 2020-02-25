# -*- coding: UTF-8 -*-

'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        known_result = {}
        queue = []
        queue.append([0, 0])
        row = len(grid)
        column = len(grid[0])
        search_list = []

        for y in range(row):
            for x in range(column):
                if grid[y][x] == 1:
                    if (x, y) not in known_result:
                        known_result[x, y] = 1
                        block = []
                        block.append([x, y])
                        search_list.append([x, y])
                        while search_list:
                            tempo_x, tempo_y = search_list.pop(0)
                            for dx, dy in direction:
                                if tempo_x+dx>=0 and tempo_x+dx<column and tempo_y+dy>=0 and tempo_y+dy<row and grid[tempo_y+dy][tempo_x+dx]==1:
                                    if (tempo_x + dx, tempo_y + dy) not in known_result:
                                        known_result[tempo_x+dx, tempo_y+dy] = known_result[tempo_x, tempo_y] + 1
                                        search_list.append([tempo_x + dx, tempo_y + dy])
                                        block.append([tempo_x + dx, tempo_y + dy])
                                        for _x, _y in block:
                                            known_result[_x, _y] = known_result[tempo_x+dx, tempo_y+dy]
        try:
            return max(known_result.values())
        except:
            return 0

class Solution2(object): # 国际版官方
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

class Solution3: # 官方递归版本
    def maxAreaOfIslandCore(self, grid, row, col):
        # 如果元素符合要求，访问当前元素
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1 and self.seen[row][col] == False:
            self.seen[row][col] = True
            up = self.maxAreaOfIslandCore(grid, row - 1, col)
            down = self.maxAreaOfIslandCore(grid, row + 1, col)
            left = self.maxAreaOfIslandCore(grid, row, col - 1)
            right = self.maxAreaOfIslandCore(grid, row, col + 1)
            return up + down + left + right + 1
        else:
            return 0

    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        # 标记数组，标记已访问过的‘岛屿’元素
        self.seen = [[False for _ in range(cols)] for _ in range(rows)]

        # 遍历矩阵
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    cur_area = self.maxAreaOfIslandCore(grid, row, col)
                    max_area = max(max_area, cur_area)
        return max_area

# TODO: ！！
class Solution4: # 手写递归
    def maxAreaOfIsland(self, grid):
        row, column = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < column and 0 <= j < row and grid[j][i] == 1:
                grid[j][i] = 0
                return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
            return 0

        result = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c]:
                    result = max(result, dfs(c, r))

        return result

if __name__ == '__main__':
    print(Solution4().maxAreaOfIsland(grid=[[0,0,0]]))
