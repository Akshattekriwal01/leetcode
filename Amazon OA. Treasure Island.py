"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

import unittest
import collections
from typing import List

class Solution:
    def minSteps(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(0, 0)]
        visited = set([(0, 0)])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                        if grid[r][c] == "D":
                            return steps
                        elif grid[r][c] == "O":
                            queue.append((r, c))
                            visited.add((r, c))


class TestSolution(unittest.TestCase):
    def test(self):
        grid = [['O', 'O', 'O', 'O'],
                ['D', 'O', 'D', 'O'],
                ['O', 'O', 'O', 'O'],
                ['X', 'D', 'D', 'O']]
        output = 5
        self.assertEqual(grid, output, "Should be 5")