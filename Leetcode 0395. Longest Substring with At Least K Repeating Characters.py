"""
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for n in range(1, 27): # number of unique characters in window
            at_least_k = 0 # number of characters of at least k in window
            unique = 0 # number of unique characters in window
            count = [0] * 26
            l = r = 0
            while r < len(s):
                if unique <= n:
                    idx = ord(s[r]) - ord("a")
                    count[idx] += 1
                    if count[idx] == 1:
                        unique += 1
                    if count[idx] == k:
                        at_least_k += 1
                    r += 1
                else:
                    idx = ord(s[l]) - ord("a")
                    count[idx] -= 1
                    if count[idx] == 0:
                        unique -= 1
                    if count[idx] == k - 1:
                        at_least_k -= 1
                    l += 1
                if n == unique == at_least_k:
                    res = max(res, r - l)
        return res

