"""
668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1   2   3
2   4   6
3   6   9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
"""

class Solution:
    def findKthNumber1(self, m: int, n: int, k: int) -> int:
        """
        binary search
        Time: O(Mlog(MN))
        Space: O(1)
        """
        def count(x):
            res = 0
            for i in range(1, m + 1):
                res += min(x // i, n)
            return res

        lo, hi = 1, m * n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findKthNumber2(self, m: int, n: int, k: int) -> int:
        """
        priority queue
        Time: O(KlogM + M) ~ O(MNlogM) in worst case
        Space: O(M)
        """
        import heapq
        heap = [(i, i) for i in range(1, m + 1)]
        heapq.heapify(heap)
        for _ in range(k):
            val, row = heapq.heappop(heap)
            if val < row * n:
                heapq.heappush(heap, (val + row, row))
        return val