"""
You are given with a string . Your task is to remove atmost two substrings of any length from the given string such that the remaining string contains vowels('a','e','i','o','u') only. Your aim is the maximise the length of the remaining string. Output the length of remaining string after removal of atmost two substrings.
NOTE: The answer may be 0, i.e. removing the entire string.

Sample:
input = "earthproblem"
output = 3

input = "letsgosomewhere"
output = 2
"""

import unittest

class Solution:
    def longestString(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and (s[l] in "aeiou" or s[r] in "aeiou"):
            if s[l] in "aeiou":
                l += 1
            if s[r] in "aeiou":
                r -= 1
        mid = curr = 0
        for i in range(l, r):
            if s[i] in "aeiou":
                curr += 1
            else:
                curr = 0
            mid = max(mid, curr)
        return l + mid + len(s) - 1 - r


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().longestString("earthproblem"), 3, 
            "Should be 3")

    def test2(self):
        self.assertEqual(Solution().longestString("letsgosomewhere"), 2,
            "Should be 2")


if __name__ == "__main__":
    unittest.main()