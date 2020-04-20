"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
"""

"""
Amazon OA: zoobie in matrix
"""
import unittest
import collections
from typing import List

class Solution:
    def minHours(self, grid: List[List[int]]) -> int:
        """
        time: O(MN)
        space: O(MN)
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        queue = collections.deque([])
        humans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                else:
                    humans += 1
        t = 0
        while humans > 0:
            t += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                        humans -= 1
                        grid[r][c] = 1
                        queue.append((r, c))
        return t

class TestSolution:
    def test(self):
        grid = [[0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]]
        self.assertEqual(Solution().minHours(grid), 2, "Should be 2")