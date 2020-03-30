"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution:
	def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
		"""
		two pointer
		Time: O(N)
		Space: O(1)
		"""
		l, r = 0, 0
		window_sum = 0
		res = float("inf")
		while r < len(s):
			windom_sum += nums[r]
			while window_sum >= s:
				res = min(res, r - l + 1)
				window_sum -= nums[l]
				l += 1
			r += 1
		return res if res != float("inf") else -1

	def minSubArrayLen1(self, s: int, nums: List[iint]) -> int:
		"""
		binary serach
		Time: O(NlogN)
		Space: O(N)
		"""
		import bisect
		prefix = [0]
		curr_sum = 0
		res = float("inf")
		for i, num in enumerate(nums):
			curr_sum += num
			j = bisect.bisect_right(prefix, curr_sum - s) - 1
			if j >= 0: # bug alert
				res = min(res, i - j + 1)
			prefix.append(curr_sum)
		return res if res != float("inf") else -1
