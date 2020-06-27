class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def neighbors(i, j):
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n:
                    yield r, c

        def index(i, j):
            return i * n + j

        uf = UnionFind(m * n + 1)
        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if i == 0:
                        uf.union(index(i, j), m * n)
                    for r, c in neighbors(i, j):
                        if A[r][c] == 1:
                            uf.union(index(i, j), index(r, c))
        ans = []
        for i, j in hits[::-1]:
            if grid[i][j] == 0:
                ans.append(0) 
            else:
                prev = uf.get_size(m * n)
                if i == 0:
                    uf.union(index(i, j), m * n)
                for r, c in neighbors(i, j):
                    if A[r][c] == 1:
                        uf.union(index(i, j), index(r, c))
                A[i][j] = 1
                curr = uf.get_size(m * n)
                ans.append(max(0, curr - prev - 1))
        return ans[::-1]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, i):
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        while root != i:
            j = self.parent[i]
            self.parent[i] = root
            i = j
        return root

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.size[root_i] < self.size[root_j]:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

    def get_size(self, i):
        return self.size[self.find(i)]