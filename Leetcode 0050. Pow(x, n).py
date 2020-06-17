"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        time: O(logN)
        space: O(1)
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        ans = 1.0
        base = x
        while n > 0:
            if n % 2 == 1:
                ans *= base
                n -= 1
            else:
                base = base * base
                n //= 2
        return ans