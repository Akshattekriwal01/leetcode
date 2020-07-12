"""
718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """dp
        time O(MN), space O(MN)
        """
        m, n = len(A), len(B)
        # dp[i][j] = max sub len between A[0:i+1] and B[0:j+1]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
        return max(max(row) for row in dp)

    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        time: O(MN), space: O(1)
        """
        m, n = len(A), len(B)
        maxLen = 0
        for i in range(m):
            currLen = 0
            k = i
            for j in range(n):
                if k == m:
                    break
                if A[k] == B[j]:
                    currLen += 1
                else:
                    currLen = 0
                k += 1
                maxLen = max(maxLen, currLen)
        for j in range(n):
            currLen = 0
            k = j
            for i in range(m):
                if k == n:
                    break
                if A[i] == B[k]:
                    currLen += 1
                else:
                    currLen = 0
                k += 1
                maxLen = max(maxLen, currLen)
        return maxLen

    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(guess):
            def rolling(A, length):
                if length == 0:
                    yield 0, 0
                    return 
                P, MOD = 113, 10 ** 9 + 7
                PINV = math.pow(P, MOD - 2, MOD)
                h, power = 0, 1
                # h = sum(P^i) % MOD
                for i in range(len(A)):
                    h = 
                    if i < length - 1:
                        h += 