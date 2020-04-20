"""
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
"""

import unittest
from typing import List

class Solution:
    def uniquePairs(self, nums: List[int], target: int) -> int:
        """
        hashset
        """
        seen = {}
        res = 0
        for num in nums:
            if num == target - num:
                if num not in seen:
                    res += 1
            else:
                if not (num in seen and target - num in seen):
                    res += 1
            seen.add(num)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 2, 45, 46, 46]
        target = 47
        output = 2
        self.assertEqual(nums, target, output, "Should be 2")

    def test2(self):
        nums = [1, 1]
        target = 2
        output = 1
        self.assertEqual(nums, target, output, "Should be 1")

    def test3(self):
        nums = [1, 5, 1, 5]
        target = 6
        output = 1
        self.assertEqual(nums, target, output, "Should be 1")