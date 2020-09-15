"""
282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        time: O(N*4^N)
        space: O(N)
        """
        ans = []
        self.backtrack(num, target, 0, 0, 0, [], ans)
        return ans
        
    def backtrack(self, num, target, i, eval, prev, path, ans):
        if i == len(num):
            if eval == target:
                ans.append("".join(path))
            return
        
        for j in range(i, len(num)):
            if j > i and num[i] == "0": 
                break
            curr = int(num[i:j+1])
            if i == 0:
                self.backtrack(num, target, j + 1, curr, curr, [str(curr)], ans)
            else:
                ## add
                path.append("+")
                path.append(str(curr))
                self.backtrack(num, target, j + 1, eval + curr, curr, path, ans)
                path.pop()
                path.pop()
                ## minus
                path.append("-")
                path.append(str(curr))
                self.backtrack(num, target, j + 1, eval - curr, -curr, path, ans)
                path.pop()
                path.pop()
                ## multiply
                path.append("*")
                path.append(str(curr))
                self.backtrack(num, target, j + 1, eval - prev + prev * curr, prev * curr, path, ans)
                path.pop()
                path.pop()
