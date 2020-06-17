"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution:
    def minRemoveToMakeValid1(self, s: str) -> str:
        stack = []
        bal = 0
        for c in s:
            if c == "(":
                bal += 1
                stack.append(c)
            elif c == ")":
                if bal > 0:
                    bal -= 1
                    tmp = [c]
                    while stack and stack[-1] != "(":
                        tmp.append(stack.pop())
                    tmp.append(stack.pop())
                    if not stack or stack[-1] == "(":
                        stack.append("".join(tmp[::-1]))
                    else:
                        stack[-1] += "".join(tmp[::-1])
            else:
                if not stack or stack[-1] == "(":
                    stack.append(c)
                else:
                    stack[-1] += c
        return "".join(c for c in stack if c != "(")

    def minRemoveToMakeValid2(self, s: str) -> str:
        bal = cnt = 0
        parsed = []
        for c in s:
            if c == "(":
                bal += 1
                cnt += 1
                parsed.append(c)
            elif c == ")":
                if bal > 0:
                    bal -= 1
                    parsed.append(c)
            else:
                parsed.append(c)
        res = []
        for c in parsed:
            if c == "(":
                if cnt > bal:
                    res.append(c)
                    cnt -= 1
            else:
                res.append(c)
        return "".join(res)