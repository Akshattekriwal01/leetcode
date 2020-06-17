"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        """
        greedy
        time: O(N)
        space: O(1)
        """
        maxSum = float("-inf")
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = num
            else: 
                currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubArray2(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], lo: int, hi: int) -> int:
        if lo == hi:
            return nums[lo]
        mid = (lo + hi) // 2
        left = self.helper(nums, lo, mid)
        right = self.helper(nums, mid + 1, hi)
        cross = self.crossSum(nums, lo, hi)
        return max(left, right, cross)

    def crossSum(self, nums: List[int], lo: int, hi: int) -> int:
        mid = (lo + hi) // 2
        left = float("-inf")
        curr = 0
        for i in range(mid, lo - 1, -1):
            curr += nums[i]
            left = max(left, curr)
        right = float("-inf")
        curr = 0
        for i in range(mid + 1, hi + 1):
            curr += nums[i]
            right = max(right, curr)
        return left + right