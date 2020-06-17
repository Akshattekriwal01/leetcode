"""
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        greedy: move head and tail toward center and find first different char.
                From here skip either the head or tail and check if rest is palindromic.
        """
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True