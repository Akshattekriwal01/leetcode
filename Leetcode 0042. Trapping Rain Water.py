"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap1(self, height: List[int]) -> int:
        """ 
        greedy
        time: O(N)
        space: O(1)
        """
        l, r = 0, len(height) - 1
        water = 0
        while l < r:
            if height[l] < height[r]:
                i = l + 1
                while i < r and height[i] < height[l]:
                    water += height[l] - height[i]
                    i += 1
                l = i
            else:
                i = r - 1
                while i > l and height[i] < height[r]:
                    water += height[r] - height[i]
                    i -= 1
                r = i
        return water

    def trap2(self, height: List[int]) -> int:
        """
        monotonic stack
        time: O(N)
        space: O(N)
        """
        stack = []
        water = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                h = height[stack.pop()]
                if stack:
                    j = stack[-1]
                    water += (i - j - 1) * (min(height[i], height[j]) - h)
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
        return water