"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        import collections
        if not rooms:
            return
        INF = 2 ** 31 - 1
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and rooms[r][c] == INF:
                        rooms[r][c] = dist
                        queue.append((r, c))