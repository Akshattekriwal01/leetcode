"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        """
        union find
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    uf.add(i * n + j)
        return uf.islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n:
                    dfs(r, c)

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands

    def numIslands3(self, grid: List[List[str]]) -> int:
        import collections
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            grid[i][j] = "0"
            queue = collections.deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        queue.append((r, c))
                        grid[r][c] = "0"
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)
        return islands



class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.id = [-1] * m * n
        self.size = [0] * m * n
        self.islands = 0

    def add(self, i):
        if self.id[i] == -1:
            self.id[i] = i
            self.size[i] = 1
            self.islands += 1
            if i % self.n > 0:
                self.union(i, i - 1)
            if i >= self.n:
                self.union(i, i - self.n)

    def find(self, i):
        if self.id[i] == -1:
            return -1
        root = i
        while root != self.id[root]:
            root = self.id[root]
        while root != i:
            j = self.id[i]
            self.id[i] = root
            i = j
        return root

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == -1 or root_j == -1 or root_i == root_j:
            return
        self.islands -= 1
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
