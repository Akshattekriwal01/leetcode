"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""
from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        try to make A or B to be all A[0], record # of rotations min(rot_A, rot_B)
        try to make A or B to be all B[0], record # of rotations min(rot_A, rot_B)
        return min of the two
        """
        def check(x):
            rot_A = rot_B = len(A)
            for a, b in zip(A, B):
                if a != x and b != x:
                    return float("inf")
                if a == x:
                    rot_A -= 1
                if b == x:
                    rot_B -= 1
            return min(rot_A, rot_B)

        min_rot = min(check(A[0]), check(B[0]))
        return min_rot if min_rot != float("inf") else -1