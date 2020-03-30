"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
"""

"""
Monotonic stack & queue summary

A common scenario of using a monotonic stack & queue is to greedy search an extreme value in an array, sometimes the extreme value may be confined in one end or both ends.

queue: if looking for extreme values about a window in an array, LC239 & LC862
stack: if looking for extreme values about the whole array, LC42 & LC84 & LC456 & LC1130 & LC1340

decreasing: if the greedy search involves local minimum in array, LC42 & LC456 & LC1130 & LC1340
increasing: if the greedy search involves local maximum in array, LC84 & LC239 & LC862
"""

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		import collections
		queue = collections.deque([])
		res = []
		for i in range(len(nums)):
			while queue and nums[i] >= nums[queue[-1]]:
				queue.pop()
			queue.append(i)
			if i - queue[0] >= k - 1:
				queue.popleft()
			if i >= k - 1:
				res.append(nums[queue[0]])
		return res