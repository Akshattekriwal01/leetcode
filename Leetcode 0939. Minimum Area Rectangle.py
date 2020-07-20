"""
939. Minimum Area Rectangle
Medium

670

130

Add to List

Share
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

import collections
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set([x for x, _ in points]))
        ny = len(set([y for _, y in points]))
        if nx == n or ny == n:
            return 0
        pos = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                pos[x].append(y)
        else:
            for x, y in points:
                pos[y].append(x)
        lastx = {}
        ans = float("inf")
        for x in sorted(pos):
            pos[x].sort()
            for i in range(len(pos[x])):
                for j in range(i + 1, len(pos[x])):
                    y1 = pos[x][i]
                    y2 = pos[x][j]
                    if (y1, y2) in lastx:
                        ans = min(ans, (y2 - y1) * (x - lastx[(y1, y2)]))
                    lastx[(y1, y2)] = x
        return ans if ans != float("inf") else 0