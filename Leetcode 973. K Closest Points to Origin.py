"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

class Solution:
    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        sorting
        time: O(NlogN)
        space: space for sorting
        """
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]

    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        quick sort/select
        time: average O(N)
        space: O(N)        
        """
        import random
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        def sort(start, end, K):
            if start >= end:
                return
            k = random.randint(start, end)
            swap(start, k)
            mid = partition(start, end)
            if K == mid - start + 1:
                return
            elif K < mid - start + 1:
                sort(start, mid - 1, K)
            else:
                sort(mid + 1, end, K - (mid - start + 1))

        def partition(start, end):
            piv = dist(start)
            i = start + 1
            for j in range(start + 1, end + 1):
                if dist(j) < piv:
                    swap(i, j)
                    i += 1
            swap(start, i - 1)
            return i - 1

        def swap(i, j):
            points[i], points[j] = points[j], points[i]

        sort(0, len(points) - 1, K)
        return points[:K]