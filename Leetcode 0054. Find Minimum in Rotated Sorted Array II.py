"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time: O(N), worst case when all values are the same
        Space: O(1) 
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1
            while lo < hi and nums[hi] == nums[hi - 1]:
                hi -= 1
            mid = lo + (hi - lo) // 2
            if nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
