"""
57. Insert Interval
Hard

1632

184

Add to List

Share
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Find the insert positions of the newInterval.
            for newIntervals[0] use end of intervals, that is newInterval[0] must be smaller than intervals[i][1]
            for newIntervals[1] use start of intervals, that is newInterval[1] must be smaller or equal to intervals[j][0]
        Boundary conditions:
            0 <= i, j <= n
        """
        n = len(intervals)
        start_idx = 0
        while start_idx < n and newInterval[0] < intervals[start_idx][1]:
            start_idx += 1
        end_idx = start_idx
        while end_idx < n and newInterval[1] <= intervals[end_idx][0]:
            end_idx += 1
        start, end = newInterval
        if start_idx < n:
            start = min(start, intervals[start_idx][0])
        if 0 <= end_idx - 1 < n:
            end = max(end, intervals[end_idx - 1][1])
        return intervals[:start_idx] + [[start, end]] + intervals[end_idx:]