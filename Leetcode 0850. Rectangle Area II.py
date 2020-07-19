"""
850. Rectangle Area II

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""

from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 0, 1
        MOD = 10 ** 9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, OPEN))
            events.append((y2, x1, x2, CLOSE))
        events.sort()
        ans = 0
        active = []
        prev_y = 0
        for y, x1, x2, typ in events:
            ans += self.getArea(active) * (y - prev_y)
            ans %= MOD
            if typ == OPEN:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y

        return ans

    def getArea(self, intervals):
        intervals.sort()
        left = 0
        ans = 0
        for x1, x2 in intervals:
            left = max(left, x1)
            ans += max(0, x2 - left)
            left = max(left, x2)
        return ans


    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        MOD = 10 ** 9 + 7
        events = []
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, OPEN))
            events.append((y2, x1, x2, CLOSE))
            X.add(x1)
            X.add(x2)
        events.sort()
        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}
        stree = SegmentTree(X)
        prev_y = 0
        covered = 0
        ans = 0
        for y, x1, x2, typ in events:
            ans += (y - prev_y) * covered
            ans %= MOD
            covered = stree.update(X, Xi[x1], Xi[x2], typ)
            prev_y = y
        return ans

class SegmentTreeNode:
    def __init__(self, start, end, X):
        """
        1. start & end are the indices of x coordinates
        2. at leaf node, start + 1 == end
        3. left.end = right.start = curr.mid
        4. count keep how many times a leaf node is "activated"
        5. count is updated when we close or open an rectangle
        6. if the leaf is activated, return the covered area by this node
        7. for non leaf nodes, its covered area is sum of its children
        """
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = None
        self.right = None
        self.cover = X[end] - X[start]
        self.count = 0
        self.active = 0

class SegmentTree:
    def __init__(self, X):
        self.X = X
        self.X_i = {x: i for i, x in enumerate(X)}
        self.root = self.build_tree(0, len(X) - 1)

    def build_tree(self, l, r):
        if l >= r:
            return None
        root = SegmentTreeNode(l, r, self.X)
        if l + 1 == r:
            return root
        mid = (l + r) // 2
        root.left = self.build_tree(l, mid)
        root.right = self.build_tree(mid, r)
        return root

    def update(self, x1, x2, val):
        def _update(root, l, r):
            if l == root.start and r == root.end:
                root.count += val
            else:
                if l < root.mid:
                    _update(root.left, l, min(root.mid, r))
                if r > root.mid:
                    _update(root.right, max(root.mid, l), r)
            if root.count > 0:
                root.active = root.cover
            else:
                root.active = ((root.left.active if root.left else 0) + 
                               (root.right.active if root.right else 0))
            return root.active
        return _update(self.root, self.X_i[x1], self.X_i[x2])