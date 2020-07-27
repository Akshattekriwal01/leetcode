"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        backtracking
        time: O(N*3^L), N == # of cells, L of length of word
        space: O(L), stack space for recursion
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, set(), word, 0):
                    return True
        return False

    def dfs(self, board, i, j, visited, word, idx):
        if idx == len(word):
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i, j) in visited:
            return False
        if board[i][j] != word[idx]:
            return False
        visited.add((i, j))
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r, c = i + di, j + dj
            if self.dfs(board, r, c, visited, word, idx + 1):
                return True
        visited.remove((i, j))
        return False