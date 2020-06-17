"""
For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

Example 1:

nums = [2, 4, 5, 7]
k = 8
Output: 5
Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]
Example 2:

nums = [1, 4, 3, 2]
k = 8
Output: 15
Explanation: 16 (2^4) - 1 (empty set) = 15
Example 3:

nums = [2, 4, 2, 5, 7]
k = 10
Output: 27
Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27
Expected O(n^2) time solution or better.
"""

import unittest
from typing import List


class Solution:
    def numSubseqNoGreaterThan(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= k:
                ans += 2 ** (r - l) # 1 + 2**0 + 2**1 + ... + 2**(r-l-1)
                l += 1
            else:
                r -= 1
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [2, 4, 5, 7]
        k = 8
        output = 5
        self.assertEqual(Solution().numSubseqNoGreaterThan(nums, k), output, "Should be 5")

    def test2(self):
        nums = [1, 4, 3, 2]
        k = 8
        output = 15
        self.assertEqual(Solution().numSubseqNoGreaterThan(nums, k), output, "Should be 15")

    def test3(self):
        nums = [2, 4, 2, 5, 7]
        k = 10
        output = 27
        self.assertEqual(Solution().numSubseqNoGreaterThan(nums, k), output, "Should be 27")


if __name__ == "__main__":
    unittest.main()