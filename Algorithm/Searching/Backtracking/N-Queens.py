# -*- coding: UTF-8 -*-

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
'''

class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        count = 0
        output = []

        def check_one(row, col):
            if 0 <= row < n and 0 <= col < n:
                if board[row][col] == '.':
                    for i in range(-n+1, n):
                        if 0 <= row + i < n and 0 <= col + i < n:
                            if board[row + i][col + i] == 'Q':
                                return False
                    for i in range(-n+1, n):
                        if 0 <= row + i < n and 0 <= col - i < n:
                            if board[row + i][col - i] == 'Q':
                                return False
                    return True
                else:
                    return False

        def check_two(row, col):
            if 0 <= row < n and 0 <= col < n:
                if board[row][col] == '.':
                    for i in range(-n+1, n):
                        if 0 <= row + i < n:
                            if board[row + i][col] == 'Q':
                                return False
                    return True
                else:
                    return False

        def could_place(row, col):
            return check_one(row, col) and check_two(row, col)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    board[row][col] = 'Q'
                    if row + 1 == n:
                        output.append(board[:])
                        board[row] = ['.'] * n
                    else:
                        backtrack(row + 1)
            board[row - 1] = ['.'] * n

        backtrack()
        for i in range(len(output)):
            for j in range(len(output[0])):
                output[i][j] = ''.join(output[i][j])
        return output

class Solution2:
    def solveNQueens(self, n):
        # used / visited 等可使用HashTable(set()) / 组[False for i xxx] /
        output = []
        dales = set()
        hills = set()
        cols = set()
        x = [i for i in range(n)]

        def __convert2board(stack, n):
            return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]

        def backtrack(row=0, stack=[]):
            if row == n:
                board = __convert2board(stack, n)
                output.append(board)
                return

            for i in range(n):
                if i not in cols and i + row not in dales and i - row not in hills:
                    cols.add(i)
                    dales.add(i + row)
                    hills.add(i - row)
                    stack.append(i)
                    backtrack(row + 1, stack)
                    cols.remove(i)
                    dales.remove(i + row)
                    hills.remove(i - row)
                    stack.pop()

        backtrack()
        return output

class Solution3:
    def solveNQueens(self, n):
        output = []
        cols = [False for _ in range(n)]
        dales = [False for _ in range(2 * n - 1)]
        hills = [False for _ in range(2 * n - 1)]
        x = [i for i in range(n)]

        def __convert2board(stack):
            return ['.' * stack[i] + 'Q' + '.' * (n - stack[i] - 1) for i in range(n)]

        def backtrack(row=0, stack=[]):
            if row == n:
                board = __convert2board(stack)
                output.append(board)
                return

            for i in range(n):
                if not cols[i] and not dales[i + row] and not hills[row - i]:
                    cols[i] = True
                    dales[i + row] = True
                    hills[row - i] = True
                    stack.append(i)
                    backtrack(row + 1, stack)
                    cols[i] = False
                    dales[i + row] = False
                    hills[row - i] = False
                    stack.pop()
        backtrack()
        return output


if __name__ == '__main__':
    board = Solution3().solveNQueens(n=4)
    for i in range(len(board)):
        print(board[i])