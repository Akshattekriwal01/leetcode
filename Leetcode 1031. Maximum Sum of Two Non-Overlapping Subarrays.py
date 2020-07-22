"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
        brute force:
            For any pos i, the L array and M array must be on the two sides of i. 
            So we can search max sum L array on the left and max sum M array on 
            the right; or max sum M array on the left and max sum L array on the right.
            time: O(N^2), space: O(1)

        dynamic programming with presum
            dp_L: dp_L[i] = max subarray sum of length L to until i
            dp_M: dp_M[i] = max subarray sum of length M to until i
            dp_LM: dp_LM[i] = max subarray sum of length L and M to until i
                L subarray ends at i => dp_LM[i] = dp_M[i-L] + sum(A[i-L+1:i+1])
                M subarray ends at i => dp_LM[i] = dp_L[i-M] + sum(A[i-M+1:i+1])
                L and M end at previous index => dp_LM[i] = dp_LM[i-1]
                take max of above three case => dp_LM[i]
            time O(N), space O(N)

        sliding window
        we can reduce space from O(N) to O(1) in two pass with similar approach to the dp solution. 
        """

        def helper(A, L, M):
            sumL = sum(A[:L]) # running sum of length L array
            sumM = sum(A[L:L+M]) # running sum of length M array
            maxL = sumL # max sum of length L array
            maxLM = maxL + sumM # max sum of the two sub arrays
            for i in range(L, len(A) - M):
                sumL += A[i] - A[i-L]
                sumM += A[i+M] - A[i]
                maxL = max(maxL, sumL)
                maxLM = max(maxLM, maxL + sumM)
            return maxLM
        
        return max(helper(A, L, M), helper(A, M, L))