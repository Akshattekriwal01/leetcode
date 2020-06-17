"""
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        l, r, u, b = 0, n - 1, 0, n - 1
        num = 1
        while l < r:
            for i in range(l, r):
                matrix[u][i] = num
                num += 1
            for i in range(u, b):
                matrix[i][r] = num
                num += 1
            for i in range(r, l, -1):
                matrix[b][i] = num
                num += 1
            for i in range(b, u, -1):
                matrix[i][l] = num
                num += 1
            l += 1
            r -= 1
            u += 1
            b -= 1
        if l == r:
            matrix[l][u] = num
        return matrix