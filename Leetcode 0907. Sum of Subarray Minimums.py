"""
907. Sum of Subarray Minimums

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left, right = [1] * n, [1] * n
        stack = []
        for i in range(n):
            while stack and stack[-1][0] > A[i]:
                left[i] += stack.pop()[1]
            stack.append((A[i], left[i]))
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= A[i]:
                right[i] += stack.pop()[1]
            stack.append((A[i], right[i]))
        return sum(a * l * r for a, l, r in zip(A, left, right))