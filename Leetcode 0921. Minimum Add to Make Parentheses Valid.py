"""
921. Minimum Add to Make Parentheses Valid

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """ use stack """
        stack = []
        ans = 0
        for c in S:
            if c == ")":
                if not stack:
                    ans += 1
                else:
                    stack.pop()
            else:
                stack.append(c)
        return ans + len(stack)

    def minAddToMakeValid(self, S: str) -> int:
        """ no extra space """
        ans = bal = 0
        for c in S:
            if c == "(":
                bal += 1
            else:
                if bal == 0:
                    ans += 1
                else:
                    bal -= 1
        return ans + bal