"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        s_count = collections.defaultdict(int)
        covered = 0
        min_sub_str = ""
        min_sub_len = float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] in t_count:
                s_count[s[r]] += 1
                if s_count == t_count[s[r]]:
                    covered += 1
            while l <= r and covered == len(t_count):
                if r - l + 1 < min_sub_len:
                    min_sub_len = r - l + 1
                    min_sub_str = s[l:r+1]
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        covered -= 1
                l += 1
        return min_sub_str