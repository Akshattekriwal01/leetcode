"""
778. Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
"""

class Solution:
    def swimInWater1(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def canSwim(T):
            # iterative dfs is faster than recursive
            # time: O(N^2)
            # space: O(N^2)
            stack = [(0, 0)]
            visited = set([(0, 0)])
            while stack:
                i, j = stack.pop()
                if i == N - 1 and j == N - 1:
                    return True
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r, c = i + di, j + dj
                    if 0 <= r < N and 0 <= c < N and grid[r][c] <= T and (r, c) not in visited:
                        visited.add((r, c))
                        stack.append((r, c))
            return False

        lo, hi = grid[0][0], N * N
        while lo < hi:
            # time: O(logN)
            mid = lo + (hi - lo) // 2
            if canSwim(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def swimInWater2(self, grid: List[List[int]]) -> int:
        """
        priority queue
        time: O(N^2logN)
        space: O(N^2)
        """
        N = len(grid)
        heap = [(grid[0][0], i, j)]
        visited = {(0, 0)}
        ans = 0
        while heap:
            d, i, j = heapq.heappop(heap)
            ans = max(ans, d)
            if i == N - 1 and j == N - 1:
                return ans
            for r, c in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= r < N and 0 <= c < N and (r, c) not in visited:
                    heapq.heappush(heap, (grid[r][c], r, c))
                    visited.add((r, c))