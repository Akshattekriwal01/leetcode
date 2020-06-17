"""
311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution:
    def multiply1(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        hash table
        time: O(LNQ)
        space: O(LP + NQ)
        """
        l, m, n = len(A), len(A[0]), len(B[0])
        a = collections.defaultdict(dict)
        b = collections.defaultdict(dict)
        for i in range(l):
            for j in range(m):
                if A[i][j] != 0:
                    a[i][j] = A[i][j]
        for i in range(m):
            for j in range(n):
                if B[i][j] != 0:
                    b[j][i] = B[i][j]
        C = [[0] * n for _ in range(l)]
        for i in range(l):
            for j in range(n):
                for k in b[j]:
                    C[i][j] += a[i].get(k, 0) * b[j][k]
        return C


    def multiply1(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        follow up: one matrix is much more sparse than the other
        time: O(LNPlogQ), P = average number of non-zero elements per row in A
                          Q = average number of non-zero elements per col in B
        space: O(LP + NQ)
        """
        l, m, n = len(A), len(A[0]), len(B[0])
        a = collections.defaultdict(list)
        b = collections.defaultdict(list)
        for i in range(l):
            for j in range(m):
                if A[i][j] != 0:
                    a[i].append((j, A[i][j]))
        for j in range(n):
            for i in range(m):
                if B[i][j] != 0:
                    b[j].append((i, B[i][j]))

        def dot(u, v):
            product = 0
            for i, x in u:
                idx = search(v, i)
                if idx >= 0:
                    product += x * v[idx][1]
            return product

        def search(v, target):
            l, r = 0, len(v) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if v[mid][0] == target:
                    return mid
                elif mid < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        C = [[0] * n for _ in range(l)]
        for i in range(l):
            for j in range(n):
                C[i][j] = dot(a[i], b[j])

        return C