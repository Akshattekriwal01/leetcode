"""
218. The Skyline Problem
Hard

2104

115

Add to List

Share
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""

import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        For each building, either at the left boundary or right boundary it
        could part of the skyline, only when this boundary changed the max 
        height prior to the point.

        We can break the building into two points (left, height) and
        (right, height) and sort all points using the x coordinates. Then,
        process points from small x to large x and in the mean time record all
        processed heights; when process a new (x, y), if it is the start of 
        building, we should try to add y to height; else, remove it from 
        heights; as we add to or remove from heights, check if that changed max
        height; if yes, add it to the skyline.
        """
        points = [] # Point(x, y, end, is_start)
        for l, r, h in buildings:
            points.append(Point(l, h, r, True)) 
            points.append(Point(r, h, r, False))
        points.sort()
        
        heights = [(0, float("inf"))] # (-h, x) max heap to keep a point
        skyline = []
        max_height = 0
        for p in points:
            if p.is_start:
                heapq.heappush(heights, (-p.y, p.end))
            else:
                while heights[0][1] <= p.x:
                    heapq.heappop(heights)
            if max_height != -heights[0][0]:
                max_height = -heights[0][0]
                skyline.append([p.x, max_height])
        return skyline

class Point:
    def __init__(self, x, y, end, is_start):
        self.x = x
        self.y = y
        self.end = end
        self.is_start = is_start
    
    def __lt__(self, p):
        if self.x != p.x:
            return self.x < p.x
        if self.is_start:
            y1 = -self.y
        else:
            y1 = self.y
        if p.is_start:
            y2 = -p.y
        else:
            y2 = p.y
        return y1 < y2