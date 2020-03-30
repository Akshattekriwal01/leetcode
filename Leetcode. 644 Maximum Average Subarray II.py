"""
644. Maximum Average Subarray II

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""

class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:
		lo, hi = -10000.0, 10000.0
		while hi - lo > 1e-5:
			mid = (lo + hi) / 2
			if self.exists(nums, k, mid):
				lo = mid
			else:
				hi = mid
		return lo
		
	def exists(self, nums, k, target):
		cumsum = 0.0
		for i in range(k):
			cumsum += nums[i] - target
		if cumsum >= 0.0:
			return True
		prev = prev_min = 0.0
		for i in range(k, len(nums)):
			cumsum += nums[i] - target
			prev += nums[i-k] - target
			prev_min = min(prev_min, prev)
			if cumsum >= prev_min:
				return True
		return False