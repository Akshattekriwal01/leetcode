# Monotonic Stack
# Time: O(N)
# Space: O(N)
class Solution:
    def largestRectangleArea(self, heights):
        """ algorithm:
                keep an stack of increasing heights,  
        """
        n = len(heights)
        stack = [-1]
        res = 0
        for i in range(n):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                res = max(res, h * (i - stack[-1] - 1))
            stack.append(i)
        while len(stack) > 1:
            h = heights[stack.pop()]
            res = max(res, h * (n - stack[-1] - 1))
        return res
# Test Cases
# test case 1: heights = [2, 1, 5, 6, 2, 3]
# i = 0, stack = [-1, 0], res = 0
# i = 1, stack = [-1, 1], res = 2
# i = 2, stack = [-1, 1, 2], res = 2
# i = 3, stack = [-1, 1, 2, 3], res = 2
# i = 4:
    # stack = [-1, 1, 2], res = max(2, 6 * 1) = 6
    # stack = [-1, 1], res = max(6, 5 * 2) = 10
    # stack = [-1, 1, 4]
# i = 5, stack = [-1, 1, 4, 5], res = 10
# final while loop:
    # stack = [-1, 1, 4], res = max(10, 3 * 1) = 10
    # stack = [-1, 1], res = max(10, 2 * 2) = 10
    # stack = [-1], res = max(10, 1 * 6) = 10