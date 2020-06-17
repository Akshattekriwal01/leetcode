"""
727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        """
        dynamic programming 2d
        dp[i][j] = min substr length end at S[i] contains T[0...j]
        """
        m, n = len(S), len(T)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if S[i] == T[j]:
                    if j == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
        min_len = min(dp[i][n] for i in range(m + 1))
        if min_len == float("inf"):
            return ""
        for i in range(1, m + 1):
            if dp[i][n] == min_len:
                return S[i-min_len:i]

        