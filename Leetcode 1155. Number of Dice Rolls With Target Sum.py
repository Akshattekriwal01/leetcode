"""
1155. Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""

import unittest


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        top-down
        """
        MOD = 10 ** 9 + 7
        def dp(i, s, memo):
            if i == d:
                return 1 if s == target else 0
            if s >= target:
                return 0
            if (i, s) not in memo:
                memo[(i, s)] = sum(dp(i + 1, s + x, memo) for x in range(1, f + 1)) % MOD
            return memo[(i, s)]

        return dp(0, 0, {})


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().numRollsToTarget(1, 6, 3), 1,
            "Should be 1")

    def test2(self):
        self.assertEqual(Solution().numRollsToTarget(2, 6, 7), 6, 
            "Should be 6")

    def test3(self):
        self.assertEqual(Solution().numRollsToTarget(2, 5, 10), 1,
            "Should be 1")

    def test4(self):
        self.assertEqual(Solution().numRollsToTarget(1, 2, 3), 0, 
            "Should be 0")

    def test5(self):
        self.assertEqual(Solution().numRollsToTarget(30, 30, 500), 222616187,
            "Should be 222616187")


if __name__ == "__main__":
    unittest.main()