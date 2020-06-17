"""
1444. Number of Ways of Cutting a Pizza

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """
        presum: running backward is much faster
        time: O(MNK)
        space: O(MNK)
        """
        M, N = len(pizza), len(pizza[0])
        MOD = 10 ** 9 + 7
        apples = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M - 1, -1 , -1):
            for j in range(N - 1, -1, -1):
                apples[i][j] = apples[i][j+1] + apples[i+1][j] - apples[i+1][j+1]
                apples[i][j] += int(pizza[i][j] == "A")

        def dfs(i, j, k, memo):
            if apples[i][j] == 0:
                return 0
            if k == 1:
                return 1
            if (i, j, k) not in memo:
                ans = 0
                for r in range(i + 1, M):
                    if apples[i][j] > apples[r][j]:
                        ans += dfs(r, j, k - 1, memo)
                for c in range(j + 1, N):
                    if apples[i][j] > apples[i][c]:
                        ans += dfs(i, c, k - 1, memo)
                memo[(i, j, k)] = ans % MOD
            return memo[(i, j, k)]
            
        return dfs(0, 0, k, {})