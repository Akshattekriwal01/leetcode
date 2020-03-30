"""
456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
"""

class Solution:
	def find132pattern(self, nums: List[int]) -> bool:
		stack = []
		num_k = float("-inf")
		for num in nums[::-1]:
			if num < num_k:
				return True
			while len(stack) > 0 and num > stack[-1]:
				num_k = stack.pop()
			stack.append(num)
		return False