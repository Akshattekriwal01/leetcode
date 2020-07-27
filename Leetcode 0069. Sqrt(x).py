"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """ binary search """
        lo, hi = 1, x
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi
    
    def mySqrt(self, x: int) -> int:
        """ 
        Newton's method:
        the problem can be translated into finding the root of f(s)=s^2-x=0
        assume currently s is at s0, if we assume the root is at s1, then 
        approximately, (f(s1) - f(s0)) / (s1 - s0) ~ f'(s0) = 2 * s0; because
        f(s1) == 0,
        s1 = s0 - f(s0) / (2 * s0) 
           = s0 - (s0^2 - x) / (2 * s0)
           = (s0 + x / s0) / 2
        """
        s0 = 1
        s1 = (s0 + x / s0) / 2
        while abs(s0 - s1) >= 1:
            s0 = s1
            s1 = (s0 + x / s0) / 2
        return int(s1)