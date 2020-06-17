"""
1358. Number of Substrings Containing All Three Characters
Medium

218

2

Add to List

Share
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""

class Solution:
    def numberOfSubstrings1(self, s: str) -> int:
        """
        two pointer: count number of substrings containing at most 3 and 2 chrs
        """
        def atMost(n: int) -> int:
            window = {}
            cnt = l = 0
            for r, c in enumerate(s):
                window[c] = window.get(c, 0) + 1
                while l <= r and len(window) > n:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                cnt += r - l + 1
            return cnt
        return atMost(3) - atMost(2)

    def numberOfSubstrings2(self, s: str) -> int:
        counts = {"a": 0, "b": 0, "c": 0}
        res = l = 0
        for r, c in enumerate(s):
            counts[c] += 1
            while all(c > 0 for c in counts.values()):
                counts[s[l]] -= 1
                l += 1
            res += l
        return res

    def numberOfSubstrings3(self, s: str) -> int:
        indices = {"a": -1, "b": -1, "c": -1}
        res = 0
        for i, c in enumerate(s):
            indices[c] = i
            res += min(indices.values()) + 1
        return res
