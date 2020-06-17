"""
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.

"""

class Solution:
    def findDiagonalOrder1(self, matrix: List[List[int]]) -> List[int]:
        """
        for loop
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        d = -1
        ans = []
        for s in range(m + n - 1):
            _min = max(0, s - n + 1)
            _max = min(s, m - 1)
            if d == -1:
                for i in range(_max, _min - 1, -1):
                    ans.append(matrix[i][s - i])
            else:
                for i in range(_min, _max + 1):
                    ans.append(matrix[i][s - i])
            d = -d
        return ans

    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:
        """
        while loop
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        ans = []
        di, dj = -1, 1
        i = j = 0
        while cnt < m * n:
            ans.append(matrix[i][j])
            cnt += 1
            if 0 <= i + di < m and 0 <= j + dj < n:
                i += di
                j += dj
            else:
                di, dj = -di, -dj
                if i + di >= m:
                    j += 1
                elif j + dj >= n:
                    i += 1
                elif i + di < 0:
                    j += 1
                elif j + dj < 0:
                    i += 1
        return ans
