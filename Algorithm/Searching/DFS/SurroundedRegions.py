# -*- coding: UTF-8 -*-

'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return

        count = 0
        R, C = len(board), len(board[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(i, j, trigger):
            if board[j][i] == 'O':
                board[j][i] = '#'

            if i == 0 or i == C - 1 or j == 0 or j == R - 1:
                if board[j][i] == 'X':
                    return True
                else:
                    return False

            if board[j][i] == '#':
                tbd.add((i, j))
                for dx, dy in directions:
                    tmp_x = i+dx
                    tmp_y = j+dy
                    if (tmp_x, tmp_y) not in tbd:
                        flag = (tmp_x == 0 or tmp_x == C - 1 or tmp_y == 0 or tmp_y == R - 1)
                        if flag == True:
                            if board[tmp_y][tmp_x] == 'O' or board[tmp_y][tmp_x] == '#':
                                trigger = False
                        elif 0 < tmp_x < C - 1 and 0 < tmp_y < R - 1:
                            trigger = dfs(tmp_x, tmp_y, trigger)
            return trigger

        for r in range(R):
            for c in range(C):
                # if (c, r) not in known_result: # 这个known_result不对
                if board[r][c] == 'O':
                    tbd = set()
                    trigger = dfs(c, r, trigger=True)
                    if trigger:
                        for m, n in iter(tbd):
                            board[n][m] = 'X'
                    else:
                        for m, n in iter(tbd):
                            board[n][m] = 'O'
        for r in range(R):
            for c in range(C):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        return board

class Solution2: # DFS
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        R, C = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < C and 0 <= j < R and board[j][i] == 'O':
                board[j][i] = 'B'
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        for c in range(C):
            dfs(c, 0)
            dfs(c, R-1)

        for r in range(R):
            dfs(0, r)
            dfs(C-1, r)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'B':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        return board

class Solution3: # BFS
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        queue = []
        R, C = len(board), len(board[0])

        def bfs(i, j):
            if 0 <= i < C and 0 <= j < R and board[j][i] == 'O':
                board[j][i] = 'B'
                queue.append((i, j))
            while queue:
                x, y = queue.pop(0)
                bfs(x+1, y)
                bfs(x, y+1)
                bfs(x-1, y)
                bfs(x, y-1)


        for c in range(C):
            bfs(c, 0)
            bfs(c, R - 1)

        for r in range(R):
            bfs(0, r)
            bfs(C - 1, r)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'B':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        return board

class Solution4: # Union-Find xxxx 失败
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        R, C = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dummy_c, dummy_r = float('-inf'), float('-inf')

        class UnionFind:
            def __init__(self, board):
                self.board = board
                self.parent = [[(i, j) for i in range(len(board[0]))] for j in range(len(board))]
                # self.parent.append(float('-inf'), float('-inf'))
                self.size = [[1 for _ in range(len(board[0]))] for _ in range(len(board))]

            def find(self, i, j):
                if (i, j) != self.parent([j][i]):
                    self.parent[j][i] = self.parent(self.parent[j][i])
                    (i, j) = self.parent([j][i])

            def union(self, i1, j1, i2, j2):
                root_i1, root_j1 = self.find(i1, j1)
                root_i2, root_j2 = self.find(i2, j2)
                if root_i1 == root_i2 and root_j1 == root_j2:
                    return
                if self.size[root_j1][root_j1] <= self.size[root_j2][root_i2]:
                    self.parent[root_j1][root_i1] = self.parent[root_j2][root_i2]
                    self.size[root_j1][root_i1] += 1
                else:
                    self.parent[root_j2][root_i2] = self.parent[root_j1][root_i1]
                    self.size[root_j2][root_i2] += 1

            def is_connected(self, i1, j1, i2, j2):
                return self.find(i1, j1) == self.find(i2, j2)

        UF = UnionFind(board)
        for c in range(C):
            for r in range(R):
                if board[r][c] == "O":
                    if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                        UF.union(c, r, dummy_c, dummy_r)
                    else:
                        for dx, dy in directions:
                            if board[r+dy][c+dx] == "O":
                                union(c, r, c+dx, r+dy)

        for r in range(R):
            for c in range(C):
                if find(dummy_x, dummy_y) == find(c, r):
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


if __name__ == '__main__':
    B = Solution4().solve(board=[["X","O","O","X","X","X","O","X","O","O"],
                                ["X","O","X","X","X","X","X","X","X","X"],
                                ["X","X","X","X","O","X","X","X","X","X"],
                                ["X","O","X","X","X","O","X","X","X","O"],
                                ["O","X","X","X","O","X","O","X","O","X"],
                                ["X","X","O","X","X","O","O","X","X","X"],
                                ["O","X","X","O","O","X","O","X","X","O"],
                                ["O","X","X","X","X","X","O","X","X","X"],
                                ["X","O","O","X","X","O","X","X","O","O"],
                                ["X","X","X","O","O","X","O","X","X","O"]])
    for r in range(len(B)):
        print(B[r])

    print('---------------------------------------------------------------')
    a = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
         ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
         ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
    for i in range(len(a)):
        print(a[i])