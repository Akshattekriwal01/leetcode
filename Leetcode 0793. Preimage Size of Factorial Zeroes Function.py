"""
793. Preimage Size of Factorial Zeroes Function

Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].
"""

class Solution:
	def preimageSizeFZF(self, K: int) -> int:
        """
        binary search
        time: O((logK)^2)
        space: O(logK)
        x! = 2^a * 5^b * ..., f(x) = min(a, b) = b
        zeta(x) = x // 5 + x // 5^2 + x // 5^3 + ...
        zeta(5a-1) < zeta(5a) = zeta(5a+1) = zeta(5a+2) = zeta(5a+3) = zeta(5a+4) < zeta(5a+5), so if zeta(x) == K, then answer is 5 else 0
        """
        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = 5 * K - 1, 5 * K + 5
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cnt = zeta(mid)
            if cnt == K:
                return 5
            elif cnt < K:
                lo = mid + 1
            else:
                hi = mid
        return 0
