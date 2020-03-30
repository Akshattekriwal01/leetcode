"""
1340. Jump Game V

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
"""
class Solution:
    def maxJumps1(self, arr: List[int], d: int) -> int:
        """
        Top down dynamic programming:
            Lets define f(i) as the max steps we can jump starting at position i. From i, we move backward or forward at most d steps or until a value greater than or equal to arr[i], dp[i] = max(dp[i], 1 + dp[j]) for all j statisfies these conditions. 
        Time: O(N*D)
        Space: O(N)
        """
        n = len(arr)
        def dp(i, memo):
            if i not in memo:
                res = 1
                for j in range(i - 1, max(0, i - d) - 1, -1):
                    if arr[j] >= arr[i]:
                        break
                    res = max(res, 1 + dp(j, memo))
                for j in range(i + 1, min(n - 1, i + d) + 1):
                    if arr[j] >= arr[i]:
                        break
                    res = max(res, 1 + dp(j, memo))
                memo[i] = res
            return memo[i]
        memo = {}
        res = 0
        for i in range(n):
            res = max(res, dfs(i, memo))
        return res

    def maxJumps2(self, arr: List[int], d: int) -> int:
        """
        Bottom up dynamic programming:
            For bottom up, we need to start build up the dp array from smallest
            value.
        Time: O(N*D)
        Space: O(N)
        """
        n = len(arr)
        dp = [1] * n
        for a, i in sorted([(a, i) for i, a in enumerate(arr)]:
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
            for j in range(i + 1, min(n - 1, i + d) + 1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def maxJumps3(self, arr: List[int], d: int) -> int:
        """
        Monotonic stack:
            Maintain a stack of indices of decreasing array values. Iterate through the array, every time there is a raise of value, pop the index of the smallest element(s) from the stack and save them in L.
            Now, the top of the stack (l) and current index (r) defines a window in which l and r can jump to, given that that satisfies the problem definition.
        Time: O(N)
        Space: O(N)
        """
        n = len(arr)
        dp = [1] * (n + 1)
        stack = []
        for i, a in enumerate(arr + [float("inf")]):
            while stack and a > arr[stack[-1]]:
                L = [stack.pop()]
                while stack and arr[stack[-1]] == arr[L[0]]:
                    L.append(stack.pop())
                for j in L:
                    if i - j <= d:
                        dp[i] = max(dp[i], 1 + dp[j])
                    if j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], 1 + dp[j])
            stack.append(i)
        return max(dp[:-1])

    def maxJumps4(self, arr: List[int], d: int) -> int:
        """
        Model the order of jumps as edges of a DAG.
        Time: O(N)
        Space: O(N)
        """
        import collections
        from functools import lru_cache
        graph = collections.defaultdict(list)

        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        graph[i].append(j)
                stack.append(i)
        jump(range(n))
        jump(reversed(range(n)))

        @lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)
        return max(map(height, range(n)))

