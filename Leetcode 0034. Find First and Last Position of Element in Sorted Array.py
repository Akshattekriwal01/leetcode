"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        first = self.searchFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.searchLast(nums, target)
        return [first, last]

    def searchFirst(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # invariant: numbers to the left of lo should all be smaller than target
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo if lo < len(nums) and nums[lo] == target else -1

    def searchLast(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # invariant: numbers to the right of hi should all be greater than target
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi if hi >= 0 and nums[hi] == target else -1