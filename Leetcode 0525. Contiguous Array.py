"""
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        time: O(N)
        space: O(N)
        """
        seen = {0: -1}
        bal = 0
        res = 0
        for i, d in enumerate(nums):
            if d == 1:
                bal += 1
            else:
                bal -= 1
            if bal in seen:
                res = max(res, i - seen[bal])
            else:
                seen[bal] = i
        return res