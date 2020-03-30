"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height: [int]) -> int:
        """
        Monotonic stack: keep a stack of decreasing height index, if there is a raise in height, accumulate trapped water by removing dips in the stack.
        """
        stack = [-1]
        water = 0
        for i in range(len(height)):
            while len(stack) > 1 and height[i] >= height[stack[-1]]:
                j = stack.pop()
                h = min(height[i], height[stack[-1]]) - height[j]
                water += h * (i - stack[-1] - 1)
            stack.append(i)
        return water