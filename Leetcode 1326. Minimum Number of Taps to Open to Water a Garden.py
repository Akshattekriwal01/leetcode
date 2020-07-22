"""
1326. Minimum Number of Taps to Open to Water a Garden

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
"""

from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        Intuition: Each tap can water an interval [i - ranges[i], i + ranges[i]]
                   the problem becomes finding a minimum number of taps that 
                   can cover [0, n]. 

        We can try a greedy approach to add new intervals if this new interval 
        could expand the covered range. All added interval's end is stored 
        using a stack in increasing order.
            1. If a new interval's start is larger than previous end, then no 
               need to add it.
            2. If a new interval's end is smaller than prevous end, then no 
               need to add it.
            3. If a new interval's start is between previous two ends, then
               it can be added by appending the end to the stack.
            4. If a new intervals' start is smaller than second most recent
               added interval's end, then it means the one added most recently
               can be removed. To do this, we can simply pop the stack. We keep
               popping the stack until this condition is not met.
            5. At the end of each iteration, we check if the top of the stack
               is equal or greater than n; if yes, return the size of the stack.
            6. If all intervals processed and we haven't reach n return -1.
        """
        stack = [] # increasing stack keeping the ends of intervals
        for i in range(n + 1):
            start, end = i - ranges[i], i + ranges[i]
            if not stack or (start <= 0 and end >= stack[-1]):
                stack = [end]
            elif start <= stack[-1] < end: # current interval can expand
                while len(stack) > 1:
                    prev = stack.pop()
                    if start > stack[-1]: # previous interval is necessary
                        stack.append(prev)
                        break
                stack.append(end)
            if stack[-1] >= n:
                return len(stack)
        return -1
    
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        This problem can be converted to Jump Game II.

        Build max_range array to store the most distance it can water. If 
        modify the ranges array in place, space can be reduced to O(1).

        Similar problems: 45 Jump Game II, 1024 Viedo Stitching
        """
        max_range = [0] * (n + 1)
        for i in range(n + 1):
            l, r = max(0, i - ranges[i]), min(n, i + ranges[i])
            max_range[l] = max(max_range[l], r - l)
        
        # can_reach: maximum position up to current tap
        # max_can_reach: maximum position can reach without open new tap
        can_reach = max_can_reach = max_range[0]
        steps = 1
        for i in range(1, n + 1):
            # at current pos i, it guranteed we can reach i - 1
            if max_can_reach < i: # cannot water i without open new tap
                if can_reach < i: # cannot water i even if open new tap
                    return -1
                steps += 1 # there are some previous tap can water i
                max_can_reach = can_reach
            if max_can_reach >= n:
                return steps
            can_reach = max(can_reach, i + max_range[i])
        return -1