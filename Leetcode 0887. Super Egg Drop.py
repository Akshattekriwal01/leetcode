"""
887. Super Egg Drop

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        Intuition: dp[n][k] = min steps to check n floors with k eggs
                   dp[n][k] = min(1 + max(dp[x-1][k-1], dp[n-x][k]) for all x)
                   time O(KN^2), space O(KN)
        """
        def dfs(n, k, memo):
            if n == 0:
                return 0
            if k == 1:
                return n
            if (n, k) not in memo:
                ans = float("inf")
                for x in range(1, n + 1):
                    ans = min(ans, 1 + max(dfs(x - 1, k - 1, memo), dfs(n - x, k, memo)))
                memo[(n, k)] = ans
            return memo[(n, k)]
        return dfs(N, K, {})
    
    def superEggDrop(self, K: int, N: int) -> int:
        """
        The above algorithm got TLE. To optimize it, one can observe that the
        number of steps increases with the number of floors. So dp[x-1][k-1] 
        increases while dp[n-x][k] decreases when we increase x. This allows us
        to binary search x for the minimum values instead of iterate all n.

        time O(KNlogN), space O(KN)
        """
        def dfs(n, k, memo):
            if n <= 1 or k == 1:
                return n
            if (n, k) not in memo:
                lo, hi = 0, n
                while lo < hi:
                    mid = (lo + hi) // 2
                    t1, t2 = dfs(mid - 1, k - 1, memo), dfs(n - mid, k, memo)
                    if t1 >= t2:
                        hi = mid
                    else:
                        lo = mid + 1
                memo[(n, k)] = 1 + max(dfs(lo - 1, k - 1, memo), dfs(n - lo, k, memo))
            return memo[(n, k)]
        return dfs(N, K, {})

    def superEggDrop(self, K: int, N: int) -> int:
        """ 
        The binary search looks for best balanced point between 0 to n each 
        time, but in fact this balance point is monotonic increasing as n 
        increases. So, it is only required to go through N once.

        time O(KN), space O(KN)
        """
        dp = [[float("inf") for _ in range(N + 1)] for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j
        
        for i in range(2, K + 1):
            f = 1
            for j in range(2, N + 1):
                while f < j + 1 and dp[i-1][f-1] < dp[i][j-f]:
                    f += 1
                dp[i][j] = 1 + dp[i-1][f-1]
        return dp[K][N]

    def superEggDrop(self, K: int, N: int) -> int:
        """ 
        Finally, we can optimize space by using rolling dp since dp[i][j]
        depends on dp[i-1][j-1].

        time O(KN), space O(N)
        """
        dp = [[float("inf") for _ in range(N + 1)] for _ in range(2)]
        for j in range(N + 1):
            dp[1][j] = j
        for i in range(2, K + 1):
            dp[i%2][0] = 0
            dp[i%2][1] = 1
            f = 1
            for j in range(2, N + 1):
                while f < j + 1 and dp[(i-1)%2][f-1] < dp[i%2][j-f]:
                    f += 1
                dp[i%2][j] = 1 + dp[(i-1)%2][f-1]
        return dp[K%2][N]

    def superEggDrop(self, K: int, N: int) -> int:
        """
        Assume we need x moves to find the egg breaking floor with 2 eggs and 
        N floors, then we should start at x floor to drop the first egg. The 
        reason is that if it breaks at x floor, then there's only 1 egg left 
        and we have to verify from 1st to x-1 floor which would take x - 1 
        moves; if it does not break, the next move should try to drop it at 
        x + (x - 1) floor because if it breaks there, then with the only egg
        left, we have to verify from x + 1 to x + (x - 2) floor which will take
        x - 2 additional moves, adding the two moves at x and x + (x - 1) floor
        to a total of x moves. With this reasoning, we could deduce that for N
        floors and 2 eggs, the x satisfies:
            x + (x - 1) + (x - 2) + ... + 1 >= N => x^2 + x >= N

        Now, consider the general case for m moves with k eggs, dp[m][k] is the
        number of floors one can check. Then, 1 + dp[m-1][k-1] is the exact 
        floor the first move should be dropped. With a similar argument like 
        the two egg case, the next move should be at 1 + dp[m-1][k-1] + dp[m-1][k]
        floor. So dp[m][k] = 1 + dp[m-1][k-1] + dp[m-1][k]
        """
        dp = [[0] * (K + 1) for _ in range(2)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m%2][k] = 1 + dp[(m-1)%2][k-1] + dp[(m-1)%2][k]
                if dp[m%2][k] >= N:
                    return m
        

    