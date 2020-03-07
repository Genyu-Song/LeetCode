# -*- coding: UTF-8 -*-

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board, word):
        if not board: return False
        R, C = len(board), len(board[0])
        visited = [[False for _ in range(C)] for _ in range(R)]

        def dfs(i, j, combination, count):
            visited[j][i] = True
            if combination == word:
                return True
            for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
                temp_i, temp_j = i + dx, j + dy
                if 0 <= temp_i < C and 0 <= temp_j < R and word[count] == board[temp_j][temp_i]:
                    if not visited[temp_j][temp_i]:
                        if dfs(temp_i, temp_j, combination + board[temp_j][temp_i], count+1):
                            return True
            visited[j][i] = False
            return False

        for j in range(R):
            for i in range(C):
                if board[j][i] == word[0]:
                    if dfs(i, j, combination=word[0], count=1):
                        return True
        return False

if __name__ == '__main__':
    print(Solution().exist(board=[["C","A","A"],
                                  ["A","A","A"],
                                  ["B","C","D"]],
                           word="AAB"))