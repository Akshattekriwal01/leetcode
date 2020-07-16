"""
835. Image Overlap
Medium

334

452

Add to List

Share
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""

class Solution:
    def largestOverlap1(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        time: O(N^6)
        space: O(N^2)
        """
        A1 = set([(r, c) for r, row in enumerate(A) for c, val in enumerate(row) if val == 1])
        B1 = set([(r, c) for r, row in enumerate(B) for c, val in enumerate(row) if val == 1])
        ans = 0
        seen = {}
        for a in A1:
            for b in B1:
                delta = (a[0] - b[0], a[1] - b[1])
                if delta not in seen:
                    seen[delta] = sum((b[0] + delta[0], b[1] + delta[1]) in A1 for b in B1)
                    ans = max(ans, seen[delta])
        return ans

    def largestOverlap1(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        time: O(N^4)
        space: O(N^2)
        """
        A1 = set([(r, c) for r, row in enumerate(A) for c, val in enumerate(row) if val == 1])
        B1 = set([(r, c) for r, row in enumerate(B) for c, val in enumerate(row) if val == 1])
        ans = 0
        seen = collections.defaultdict(int)
        for a in A1:
            for b in B1:
                delta = (a[0] - b[0], a[1] - b[1])
                seen[delta] += 1
                ans = max(ans, seen[delta])
        return ans