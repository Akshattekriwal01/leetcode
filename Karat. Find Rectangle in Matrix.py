"""
Given a matrix with 0 or 1 as elements. Find the rectangle which contains only
ones. Return the top left corner and right bottom corner.
"""

import unittest
from typing import List


class Solution:
    def findRectangle(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    return self.helper(matrix, i, j)
                    
    def helper(self, matrix: List[List[int]], top: int, left: int) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        bottom, right = top, left
        while bottom + 1 < m and matrix[bottom+1][left] == 1:
            bottom += 1
        while right + 1 < n and matrix[top][right+1] == 1:
            right += 1
        return [top, left, bottom, right]

    def findAllRectangles(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and self.isTopLeft(matrix, i, j):
                    ans.append(self.helper(matrix, i, j))
        return ans

    def isTopLeft(self, matrix: List[List[int]], row: int, col: int) -> bool:
        if (row == 0 or matrix[row-1][col] == 0) and (col == 0 or matrix[row][col-1] == 0):
            return True
        return False

class TestSolution(unittest.TestCase):
    def testFindRectangle(self):
        matrix = [
            [0,0,1,1,1,0,0],
            [0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0]
        ]
        output = [0, 2, 1, 4]
        self.assertEqual(
            Solution().findRectangle(matrix), 
            output,
            "should be equal."
        )

    def testFindAllRectangles(self):
        matrix = [
            [0,0,1,1,1,0,0,1,0],
            [0,0,1,1,1,0,0,0,0],
            [1,1,0,0,0,0,0,0,0],
            [1,1,0,0,0,1,1,0,0],
            [0,0,0,0,0,1,1,0,0]
        ]
        output = [
            [0,2,1,4],
            [0,7,0,7],
            [2,0,3,1],
            [3,5,4,6]
        ]
        self.assertEqual(
            Solution().findAllRectangles(matrix),
            output,
            "should be equal."
        )

if __name__ == "__main__":
    unittest.main()