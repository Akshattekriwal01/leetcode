"""
1504. Count Submatrices With All Ones
Medium

148

7

Add to List

Share
Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
        def helper(arr):
            ans = 0
            l, r = -1, 0
            while r < len(arr):
                if arr[r] == 0:
                    l = r
                    r += 1
                else:
                    while r < len(arr) and arr[r] == 1:
                        r += 1
                    w = r - l - 1
                    ans += w * (w + 1) // 2
                    l = r 
            return ans

        ans = 0
        m, n = len(mat), len(mat[0])
        for up in range(m):
            arr = [1] * n
            for down in range(up, m):
                for col in range(n):
                    arr[col] &= mat[down][col]
                ans += helper(arr)
        return ans


    def numSubmat(self, mat: List[List[int]]) -> int:
        def helper(arr):
            n = len(arr)
            stack = []
            dp = [0] * n # dp[i] = # of submatrix use j as right bottom corner
            for r in range(n):
                while stack and arr[r] <= arr[stack[-1]]:
                    stack.pop()
                if stack:
                    l = stack[-1]
                    dp[r] = dp[l] # expand from previous lower height rectangles
                    dp[r] += arr[r] * (r - l) # rectangles higher than previous rectangles
                else:
                    dp[r] += arr[r] * (r + 1)
                stack.append(r)
            return sum(dp)

        ans = 0
        m, n = len(mat), len(mat[0])
        hist = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    hist[j] += 1
                else:
                    hist[j] = 0
                ans += helper(hist)
        return ans