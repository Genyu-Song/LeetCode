# -*- coding: UTF-8 -*-

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
'''

from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def could_place(row, col, d):
            return (d not in rows[row]
                    and d not in columns[col]
                    and d not in boxes[box_index(row, col)])

        def place_number(row, col, d):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(row, col, d):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_number(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(row, col, d):
                        place_number(row, col, d)
                        place_next_number(row, col)
                        if not sudoku_solved:
                            remove_number(row, col, d)
            else:
                place_next_number(row, col)

        n = 3
        N = n*n
        box_index = lambda row, col: (row // n) * n + (col // n)
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(i, j, d)

        sudoku_solved = False
        backtrack()

        return board

class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        N = len(board)
        rows = [set(range(1, 10)) for _ in range(N)]
        columns = [set(range(1, 10)) for _ in range(N)]
        boxes = [set(range(1, 10)) for _ in range(N)]
        box_index = lambda row, col: (row // 3) * 3 + col // 3

        empty = []
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    rows[i].remove(d)
                    columns[j].remove(d)
                    boxes[box_index(i, j)].remove(d)
                else:
                    empty.append([i, j])

        def backtrack(iter=0):
            if iter == len(empty):
                return True
            row, col = empty[iter]
            for d in rows[row] & columns[col] & boxes[box_index(row, col)]:
                rows[row].remove(d)
                columns[col].remove(d)
                boxes[box_index(row, col)].remove(d)
                board[row][col] = str(d)
                if backtrack(iter+1):
                    return True
                rows[row].add(d)
                columns[col].add(d)
                boxes[box_index(row, col)].add(d)
                board[row][col] = '.'
            return False

        backtrack()
        return board



if __name__ == '__main__':
    board = Solution2().solveSudoku(board=[["5","3",".",".","7",".",".",".","."],
                                          ["6",".",".","1","9","5",".",".","."],
                                          [".","9","8",".",".",".",".","6","."],
                                          ["8",".",".",".","6",".",".",".","3"],
                                          ["4",".",".","8",".","3",".",".","1"],
                                          ["7",".",".",".","2",".",".",".","6"],
                                          [".","6",".",".",".",".","2","8","."],
                                          [".",".",".","4","1","9",".",".","5"],
                                          [".",".",".",".","8",".",".","7","9"]])
    for i in range(len(board)):
        print(board[i])