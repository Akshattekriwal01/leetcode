"""
741. Cherry Pickup

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        We may choose to do two pass on the matrix with the intension
        to maximize the first path sum and then maximize the second path sum. 
        This is simple to come up however a wrong solution. Because maximize
        the first path might lead to much lower gains on the second path; or
        we may sacrifice some gain in the first path and collect more gain 
        from the second path. 

        A correct answer needs to consider the two paths simultaneously. Because
        symmetry, we can consider both path from top left to bottom right. So,
        the state of two paths can be characterized using (row1,col1,row2,col2). 
        Furthermore, because for a fixed number of steps, the row + col should 
        be constant, this effectively reduce free parameters from 4 to 3, that
        is row1 + col1 = row2 + col2.

        We can solve this problem using 3D dp:
            state: (row1, col1, row2), col2 = row1 + col1 - row2
            dp: dp(row1, col1, row2) max cherries collected with the two
                paths end at (row1, col1) and (row2, col2)
            state transition:
                dp(row1, col1, row2) = max(
                    dp(row1 - 1, col1, row2 - 1),
                    dp(row1 - 1, col1, row2),
                    dp(row1, col1 - 1, row2 - 1),
                    dp(row1, col1 - 1, row2)
                ) + grid[row1][col1] + grid[row2][col2] if row1 != row2 else grid[row1][col2]
        """
        def dp(row1, col1, row2, memo):
            col2 = row1 + col1 - row2
            if row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
                return float("-inf")
            if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return float("-inf")
            if row1 == 0 and col1 == 0:
                return grid[row1][col1]
            if (row1, col1, row2) not in memo:
                col2 = row1 + col1 - row2
                ans = grid[row1][col1]
                if row1 != row2:
                    ans += grid[row2][col2]
                ans += max(
                    dp(row1 - 1, col1, row2 - 1, memo),
                    dp(row1 - 1, col1, row2, memo),
                    dp(row1, col1 - 1, row2 - 1, memo),
                    dp(row1, col1 - 1, row2, memo)
                )
                memo[(row1, col1, row2)] = ans
            return memo[(row1, col1, row2)]
        n = len(grid)
        return max(dp(n-1, n-1, n-1, {}), 0)
