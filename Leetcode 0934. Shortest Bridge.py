"""
934. Shortest Bridge

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: A = [[0,1],[1,0]]
Output: 1
Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        r, c = self.firstOne(A)
        ones = collections.deque([(r, c)])
        zeros = collections.deque()
        visited = set([(r, c)])
        while ones:
            i, j = ones.popleft()
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    visited.add((r, c))
                    if A[r][c] == 1:
                        ones.append((r, c))
                    else:
                        zeros.append((r, c))
        depth = 0
        while zeros:
            depth += 1
            for _ in range(len(zeros)):
                i, j = zeros.popleft()
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                        visited.add((r, c))
                        if A[r][c] == 1:
                            return depth
                        zeros.append((r, c))


    def firstOne(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    return i, j