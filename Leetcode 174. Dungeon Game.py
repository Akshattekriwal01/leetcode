"""
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""

class Solution:
	def calculateMinimumHP1(self, dungeon):
		"""
		dynamic programming: 
			let dp[i][j] be the minimum health point required for cell (i, j);
			dp[i][j] = min(max(1, dp[i+1][j] - dungeon[i][j]), max(1, dp[i][j+1] - dungeon[i][j]))
		"""
		m, n = len(dungeon), len(dungeon[0])
		dp = [[1] * n for i in range(m)]
		dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
		for i in range(m - 2, -1, -1):
			dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
		for j in range(n - 1, -1, -1):
			dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
		for i in range(m - 2, -1, -1):
			for j in range(n - 1, -1, -1):
				dp[i][j] = min(
					max(1, dp[i][j+1] - dungeon[i][j]), 
					max(1, dp[i+1][j] - dungeon[i][j])
				)
		return dp[0][0]

	def calculateMinimumHP1(self, dungeon):
		"""
		binary search
		"""
		m, n = len(dungeon), len(dungeon[0])
		def canSurvive(h):
			MIN = float("-inf")
			dp = [[MIN] * (n + 1) for i in range(m+1)]
			dp[1][0] = dp[0][1] = h
			for i in range(1, m + 1):
				for j in range(1, n + 1):
					dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dungeon[i-1][j-1]
					if dp[i][j] <= 0:
						dp[i][j] = MIN
			return dp[m][n] > 0

		lo, hi = 1, 2 ** 31 - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if canSurvive(mid):
				hi = mid
			else:
				lo = mid + 1
		return lo

