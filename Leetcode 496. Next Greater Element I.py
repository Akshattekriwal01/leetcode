"""
496. Next Greater Element I
Easy

1255

1845

Add to List

Share
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
"""
class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
		num2index = {num: i for i, num in enumerate(nums1)}
		res = [-1] * len(nums1)
		stack = []
		for num in nums2:
			while stack and num > stack[-1]:
				x = stack.pop()
				if x in num2index:
					res[num2index[x]] = num
			stack.append(num)
		return res