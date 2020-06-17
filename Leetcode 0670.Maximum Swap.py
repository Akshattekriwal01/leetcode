"""
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

class Solution:
    def maximumSwap1(self, num: int) -> int:
        """
        brute force
        time: O(N^3)
        space: O(N)
        """
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans:
                    ans = A[:]
                A[i], A[j] = A[j], A[i]
        return int("".join(ans))

    def maximumSwap2(self, num: int) -> int:
        """
        greedy
        time: O(N)
        space: O(N)
        """
        A = list(str(num))
        last_indices = {int(d): i for i, d in enumerate(A)}
        for i in range(len(A)):
            for d in range(9, int(A[i]), -1):
                j = last_indices.get(d, -1)
                if j > i:
                    A[i], A[j] = A[j], A[i]
                    return int("".join(A))
        return num

