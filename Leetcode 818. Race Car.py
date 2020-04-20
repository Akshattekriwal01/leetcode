"""
818. Race Car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
 

Note:

1 <= target <= 10000.
"""

class Solution:
    def racecar1(self, target: int) -> int:
        """
        top down dynamic programming
        time: O(TlogT)
        space: O(logT)
        """
        def dfs(x, memo):
            if x == 0:
                return 0
            n = x.bit_length()
            if x == (1 << n) - 1:
                return n
            if x not in memo:
                # move n steps forward then turn back
                # command A^nR
                res = n + 1 + dfs((1 << n) - 1 - x, memo)
                # move n - 1 steps forward then turn back and move m steps
                # command A^(n-1)RA^mR...
                for m in range(n - 1):
                    res = min(res, n + m + 1 + dfs(x - (1 << (n - 1)) + (1 << m), memo))
                memo[x] = res
            return memo[x]
        return dfs(target, {})

    def racecar2(self, target: int) -> int:
        """
        bottom up dynamic programming
        time: O(TlogT)
        space: O(T)
        """
        dp = [0] + [float("inf")] * target
        for i in range(1, target + 1):
            l = i.bit_length()
            if i == (1 << l) - 1:
                dp[i] = l
            else:
                dp[i] = l + 1 + dp[(1 << l) - 1 - i]
                for j in range(l - 1):
                    dp[i] = min(dp[i], l + j + 1 + dp[i - (1 << (l - 1)) + (1 << m)])
        return dp[target]

    def racecar3(self, target: int) -> int:
        """
        dijkstra
        """
