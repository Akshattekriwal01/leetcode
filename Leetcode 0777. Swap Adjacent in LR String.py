"""
777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
 

Constraints:

1 <= len(start) == len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""
import collections

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        Intuition: we can ignore all "X" and only check for "L" & "R". 
            1. The order of "L", "R" in start, end should be the same.
            2. For "L", the index in start should be no less than that of end.
               For "R", the index in start should be no more than that of start.
        time/space O(N)
        """
        deq1 = collections.deque() # (char, idx) for start
        deq2 = collections.deque() # (char, idx) for end
        for i in range(len(start)):
            a, b = start[i], end[i]
            if a != "X":
                deq1.append((a, i))
            if b != "X":
                deq2.append((b, i))
            while deq1 and deq2:
                if deq1[0][0] != deq2[0][0]:
                    return False
                elif deq1[0][0] == "L" and deq1[0][1] < deq2[0][1]:
                    return False
                elif deq1[0][0] == "R" and deq1[0][1] > deq2[0][1]:
                    return False
                else:
                    deq1.popleft()
                    deq2.popleft()
        return len(deq1) == 0 and len(deq2) == 0

    def canTransform(self, start: str, end: str) -> bool:
        """
        optimize space to O(1) using two pointers
        """
        n = len(start)
        i, j = 0, 0
        while i < n and j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and end[j] == "X":
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                elif start[i] == "L" and i < j:
                    return False
                elif start[i] == "R" and i > j:
                    return False
                else:
                    i += 1
                    j += 1
        while i < n and start[i] == "X": i += 1
        while j < n and end[j] == "X": j += 1
        return i == n and j == n