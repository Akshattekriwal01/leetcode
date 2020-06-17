"""
679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        visited = [False] * 4
        return self.backtrack(nums, visited, 4)

    def backtrack(self, nums, visited, available):
        if available == 1:
            for i in range(4):
                if not visited[i] and abs(nums[i] - 24) < 1e-6:
                    return True
        for i in range(4):
            if not visited[i]:
                prev = nums[i]
                for j in range(i + 1, 4):
                    if not visited[j]:
                        visited[j] = True
                        # plus
                        nums[i] = prev + nums[j]
                        if self.backtrack(nums, visited, available - 1):
                            return True
                        # minus
                        nums[i] = prev - nums[j]
                        if self.backtrack(nums, visited, available - 1):
                            return True
                        nums[i] = nums[j] - prev
                        if self.backtrack(nums, visited, available - 1):
                            return True
                        # multiply
                        nums[i] = prev * nums[j]
                        if self.backtrack(nums, visited, available - 1):
                            return True
                        # divide
                        if nums[j] != 0:
                            nums[i] = prev / nums[j]
                            if self.backtrack(nums, visited, available - 1):
                                return True
                        if prev != 0:
                            nums[i] = nums[j] / prev
                            if self.backtrack(nums, visited, available - 1):
                                return True
                        visited[j] = False
                nums[i] = prev
        return False