"""
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

Don't include the first or final entry. You can only move either down or right at any point in time.

Example 1:

Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
Example 2:

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4.
"""

import unittest
from typing import List

class Solution:
    def maxMinAltitudes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = float("inf")
        for i in range(1, m):
            dp[i][0] = min(grid[i][0], dp[i-1][0])
        for j in range(1, n):
            dp[0][j] = min(gird[0][j], dp[0][j-1])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(grid[i][j], max(dp[i-1][j], dp[i][j-1]))
        if m == 1:
            return dp[-1][-2]
        if n == 1:
            return dp[-2][-1]
        return max(dp[-1][-2], dp[-2][-1])

class TestSolution(unittest.TestCase):
    def test1(self):
        grid = [[5, 1], [4, 5]]
        output = 4
        self.assertEqual(grid, output, "Should be 4")

    def test2(self):
        grid = [[1, 2, 3], [4, 5, 1]]
        output = 4
        self.assertEqual(grid, output, "Should be 4")