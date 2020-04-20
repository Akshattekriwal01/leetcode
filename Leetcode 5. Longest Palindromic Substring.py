"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """
        expand around center
        time: O(N^2)
        space: O(1)
        """
        def expand(self, s: str, l: int, r: int) -> int:
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            pal = expand(s, i, i)
            if len(pal) > len(res):
                res = pal
            pal = expand(s, i, i + 1)
            if len(pal) > len(res):
                res = pal
        return res

    def longestPalindrome2(self, s: str) -> str:
        """
        dynamic programming:
        time: O(N)
        space: O(N)
        """
        S = "@#" + "#".join(s) + "#$"
        dp = [0] * len(S)
        res, L = "", 0
        center, right = 0, 0
        for i in range(1, len(S) - 1):
            j = 2 * center - i
            if i < right:
                dp[i] = min(dp[j], right - i)
            while S[i - dp[i] - 1] == S[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center, right = i, i + dp[i]
            if dp[i] > L:
                L = dp[i]
                res = S[i - dp[i] + 1: i + dp[i]: 2]
        return res