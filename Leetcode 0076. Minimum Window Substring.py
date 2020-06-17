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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        s_count = {}
        ans = None
        l = r = seen = 0
        while r < len(s):
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r], 0) + 1
                if s_count[s[r]] == t_count[s[r]]:
                    seen += 1
            while l <= r and seen == len(t_count):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l:r+1]
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        seen -= 1
                l += 1
            r += 1
        return ans if ans else ""
