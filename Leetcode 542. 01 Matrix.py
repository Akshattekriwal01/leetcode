"""
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        queue = collections.deque()
        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                else:
                    count += 1
        d = 0
        while queue:
            d += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= r < m and 0 <= c < n:
                        if matrix[r][c] == 1 and dist[r][c] == 0:
                            dist[r][c] = d
                            count -= 1
                        if (r, c) not in visited:
                            visited.add((r, c))
                            queue.append((r, c))
            if count == 0:
                return dist