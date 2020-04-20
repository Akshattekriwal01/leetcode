"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
"""

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        largest = 0
        res = []
        for i, num in enumerate(nums):
            if target - 30 - num in seen:
                if max(num, target - 30 - num) > largest:
                    res = [seen[target - 30 - num], i]
                    largest = max(num, target - 30 - num)
            seen[num] = i
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 10, 25, 35, 60]
        target = 90
        output = [2, 3]
        self.assertEqual(nums, target, output, "Should be [2, 3]")

    def test2(self):
        nums = [20, 50, 40, 25, 30, 10]
        target = 90
        output = [1, 5]
        self.assertEqual(nums, target, output, "Should be [1, 5]")