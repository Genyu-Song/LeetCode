from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        R, C = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = []
        memo = []

        def bfs(i, j, trigger=True):
            memo = []
            queue.append([i, j])
            memo.append([i, j])
            while queue:
                i, j = queue.pop(0)
                if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                    trigger = False
                for di, dj in directions:
                    tmp_i = i + di
                    tmp_j = j + dj
                    if 0 <= tmp_i < R and j <= tmp_j < C and board[tmp_i][tmp_j] == 'O' and [tmp_i, tmp_j] not in memo:
                        memo.append([tmp_i, tmp_j])
                        queue.append([tmp_i, tmp_j])
            return memo, trigger

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    memo, trigger = bfs(i, j)
                    if trigger:
                        for m, n in memo:
                            board[m][n] = 'X'
                    else:
                        for m, n in memo:
                            board[m][n] = 'B'

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'B':
                    board[i][j] = 'O'

        for i in range(R):
            print(board[i])

if __name__ == '__main__':
    print(Solution().solve([["O","O","O","O","X","X"],
                            ["O","O","O","O","O","O"],
                            ["O","X","O","X","O","O"],
                            ["O","X","O","O","X","O"],
                            ["O","X","O","X","O","O"],
                            ["O","X","O","O","O","O"]]))