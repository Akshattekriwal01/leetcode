"""
317. Shortest Distance from All Buildings
Hard

844

53

Add to List

Share
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

"""
import collections
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        reached = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
        
        def bfs(i, j):
            visited = set()
            q = collections.deque([(i, j, 0)])
            while q:
                i, j, d = q.popleft()
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                        visited.add((r, c))
                        dist[r][c] += d
                        reached[r][c] += 1
                        q.append((r, c, d + 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        min_dist = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reached[i][j] == cnt:
                    min_dist = min(min_dist, dist[i][j])
        return min_dist if min_dist != float("inf") else -1
