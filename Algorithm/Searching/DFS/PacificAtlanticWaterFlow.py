# -*- coding: UTF-8 -*-

'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
'''

class Solution:
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0: return []
        R, C = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = []

        def dfs_pacific(i, j, flag_pacific, route):
            route.append([i, j])
            if j == 0 or i == 0:
                return True

            for di, dj in directions:
                temp_i, temp_j = i + di, j + dj
                if [temp_i, temp_j] not in route:
                    if 0 <= temp_i < C and 0 <= temp_j < R and matrix[temp_j][temp_i] <= matrix[j][i]:
                        flag_pacific = dfs_pacific(temp_i, temp_j, flag_pacific, route)
                        if flag_pacific:
                            return flag_pacific
            return flag_pacific

        def dfs_atlantic(i, j, flag_atlantic, route):
            route.append([i, j])
            if j == R - 1 or i == C - 1:
                return True

            for di, dj in directions:
                temp_i, temp_j = i + di, j + dj
                if [temp_i, temp_j] not in route:
                    if 0 <= temp_i < C and 0 <= temp_j < R and matrix[temp_j][temp_i] <= matrix[j][i]:
                        flag_atlantic = dfs_atlantic(temp_i, temp_j, flag_atlantic, route)
                        if flag_atlantic:
                            return flag_atlantic
            return flag_atlantic


        for r in range(R):
            for c in range(C):
                flag_pacific = flag_atlantic = False
                route = []
                flag_pacific = dfs_pacific(c, r, flag_pacific, route)
                route = []
                flag_atlantic = dfs_atlantic(c, r, flag_atlantic, route)
                if flag_pacific and flag_atlantic:
                    res.append([r, c])
        return res

class Solution2: # DFS超时？？
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0: return []
        R, C = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        atlantic = [[0] * C for i in range(R)]
        pacific = [[0] * C for i in range(R)]
        res = []

        def dfs(i, j, flag): # flag == True ==> Atlantic / flag == False ==> Pacific
            visited.append([j, i])
            if flag == True:
                atlantic[j][i] = 1
            else:
                pacific[j][i] = 1
            for dx, dy in directions:
                temp_x, temp_y = i+dx, j+dy
                if [temp_y, temp_x] not in visited:
                    if 0 <= temp_y < R and 0 <= temp_x < C and matrix[temp_y][temp_x] >= matrix[j][i]:
                        dfs(temp_x, temp_y, flag)

        for c in range(C):
            visited = []
            dfs(c, 0, flag=False)
            visited = []
            dfs(c, R-1, flag=True)
        for r in range(R):
            visited = []
            dfs(0, r, flag=False)
            visited = []
            dfs(C-1, r, flag=True)

        for r in range(R):
            for c in range(C):
                if atlantic[r][c] and pacific[r][c]:
                    res.append([r, c])

        return res

class Solution3: # BFS
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0: return []
        R, C = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        atlantic = [[0] * C for i in range(R)]
        pacific = [[0] * C for i in range(R)]
        visited_atlantic = []
        visited_pacific = []
        queue = []
        res = []

        def bfs(i, j, flag):
            queue.append([i, j])
            while queue:
                i, j = queue.pop(0)
                if flag == True:
                    if [i, j] not in visited_atlantic:
                        visited_atlantic.append([i, j])
                        atlantic[j][i] = 1
                        for dx, dy in directions:
                            temp_i, temp_j = i + dx, j + dy
                            if 0 <= temp_i < C and 0 <= temp_j < R and matrix[temp_j][temp_i] >= matrix[j][i]:
                                queue.append([temp_i, temp_j])
                else:
                    if [i, j] not in visited_pacific:
                        visited_pacific.append([i, j])
                        pacific[j][i] = 1
                        for dx, dy in directions:
                            temp_i, temp_j = i + dx, j + dy
                            if 0 <= temp_i < C and 0 <= temp_j < R and matrix[temp_j][temp_i] >= matrix[j][i]:
                                queue.append([temp_i, temp_j])

        for c in range(C):
            bfs(c, 0, flag=False)
            bfs(c, R-1, flag=True)

        for r in range(R):
            bfs(0, r, flag=False)
            bfs(C-1, r, flag=True)

        for r in range(R):
            for c in range(C):
                if atlantic[r][c] and pacific[r][c]:
                    res.append([r, c])

        return res

if __name__ == '__main__':
    print(Solution3().pacificAtlantic(matrix=[[1,2,2,3,5],
                                             [3,2,3,4,4],
                                             [2,4,5,3,1],
                                             [6,7,1,4,5],
                                             [5,1,1,2,4]]))