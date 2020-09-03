"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
import collections
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]: 
        left_to_remove = right_to_remove = 0
        for c in s:
            if c == "(":
                left_to_remove += 1
            if c == ")":
                if left_to_remove > 0:
                    left_to_remove -= 1
                else:
                    right_to_remove += 1
        res = []
        self.backtrack(s, 0, 0, 0, left_to_remove, right_to_remove, [], res)
        return res

    def backtrack(self, s, i, left, right, left_to_remove, right_to_remove, path, res):
        if i == len(s) and left_to_remove == 0 and right_to_remove == 0:
            res.append("".join(path))
        if i == len(s) or left_to_remove < 0 or right_to_remove < 0 or left < right:
            return
            
        if s[i] == "(":
            self.backtrack(s, i + 1, left, right, left_to_remove - 1, right_to_remove, path, res)
            self.backtrack(s, i + 1, left + 1, right, left_to_remove, right_to_remove, path + ["("], res)
        elif s[i] == ")":
            self.backtrack(s, i + 1, left, right, left_to_remove, right_to_remove - 1, path, res)
            self.backtrack(s, i + 1, left, right + 1, left_to_remove, right_to_remove, path + [")"], res)
        else:
            self.backtrack(s, i + 1, left, right, left_to_remove, right_to_remove, path + [s[i]], res)

    def removeInvalidParentheses(self, s: str) -> List[str]: 
        def isValid(string: str) -> bool:
            bal = 0
            for c in string:
                if c == "(":
                    bal += 1
                if c == ")":
                    bal -= 1
            return bal == 0
        
        ans = set()
        queue = collections.deque([s])
        while queue:
            for _ in range(len(queue)):
                s = queue.popleft()
                if isValid(s):
                    ans.add(s)
                for i in range(len(s)):
                    queue.append(s[:i] + s[i+1:])
            if len(ans) > 0:
                return list(ans)
        return [""]