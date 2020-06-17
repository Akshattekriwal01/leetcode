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

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        time: O(N*4^N)
        space: O(N)
        """
        if not num:
            return []
        self.ans = []
        self.dfs(nu, target, 1, [nums[0]], 0, 1, int(nums[0]))
        return self.ans

    def dfs(self, num, target, idx, path, x, y, z):
        """
        @params:
            idx: index of current digit
            path: current sequence of numbers and operators
            x: variable to hold result upto the last "+/-" operator
            y: variable to hold partial result from last "+/-"" to the last "*"
            z: variable to hold the number from last "*" upto current index
        """
        if idx == len(num):
            if x + y * z == target:
                self.ans.append("".join(path))
            return
        if z != 0:
            self.dfs(num, target, idx + 1, path[:-1] + [path[-1] + num[idx]],
                x, y, z * 10 + int(num[idx]))
        self.dfs(num, target, idx + 1, path + ["*"] + [nums[idx]], 
            x, y * z, int(num[idx]))
        self.dfs(num, target, idx + 1, path + ["+"] + [nums[idx]],
            x + y * z, 1, int(num[idx]))
        self.dfs(num, target, idx + 1, path + ["-"] + [nums[idx]], 
            x + y * z, -1, int(num[idx]))