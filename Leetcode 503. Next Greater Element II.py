"""
503. Next Greater Element II
Medium

1143

57

Add to List

Share
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
"""

# Time: O(N)
# Space: O(N)
class Solution:
	def nextGreaterElements(self, nums: List[int]) -> List[int]:
		"""
		Monotonic stack
		"""
		n = len(nums)
		res = [-1] * n
		stack = []
		for i in range(n):
			while stack and nums[i] > nums[stack[-1]]:
				j = stack.pop()
				res[j] = nums[i]
			stack.append(i)
		for i in range(n):
			while stack and nums[i] > nums[stack[-1]]:
				j = stack.pop()
				if res[j] == -1:
					res[j] = nums[i]
			stack.append(i)
		return res