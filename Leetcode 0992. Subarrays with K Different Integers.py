"""
992. Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMost(A, K) - self.atMost(A, K - 1)

    def atMost(self, A: List[int], K: int) -> int:
        res = 0
        counts = {}
        l = 0
        for r, a in enumerate(A):
            counts[a] = counts.get(a, 0) + 1
            while len(counts) > K:
                counts[A[l]] -= 1
                if counts[A[l]] == 0:
                    del counts[A[l]]
                l += 1
            res += r - l + 1
        return res
