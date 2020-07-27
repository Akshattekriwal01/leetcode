"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        backtracking
        time: O(M*(4*3^(L-1)))
        """
        m, n = len(board), len(board[0])
        self.root = TrieNode()
        for word in words:
            self.add(word)
        ans = set()
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, self.root, set(), [], ans)
        return list(ans)

    def add(self, word):
        node = self.root
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def dfs(self, board, i, j, node, visited, path, ans):
        m, n = len(board), len(board[0])
        if node.isWord:
            ans.add("".join(path))
        if i < 0 or i == m or j < 0 or j == n:
            return 
        if board[i][j] not in node.children or (i, j) in visited:
            return
        child = node.children[board[i][j]]
        visited.add((i, j))
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r, c = i + di, j + dj
            self.dfs(board, r, c, child, visited, path + [board[i][j]], ans)
        visited.remove((i, j))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False