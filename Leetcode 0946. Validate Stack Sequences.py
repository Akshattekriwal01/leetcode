"""
946. Validate Stack Sequences
Medium

683

21

Add to List

Share
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""
import unittest
from typing import List

class Solution:
    def validateStackSequence(self, pushed: List[int], popped: List[int]) -> bool:
        """ simulation using stack """
        n = len(popped)
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while i < n  and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == n
        
    def validateStackSequence2(self, n: int, popped: List[int]) -> bool:
        """ 
        follow up
        space O(1)

        1,2,3,4,5
        3,2, 4,1, 5 valid
        3,2, 4, 5,1 valid
        3,2, 5,4,1  valid
        3,2, 5,1, 4 invalid
        3,2,1, 4, 5 valid
        3,2,1, 5,4  valid

        """
        ptr = -1
        for i, x in enumerate(popped):


class TestSolution(unittest.TestCase):
    def test(self):
        import random
        n = 10
        pushed = [i for i in range(1, n + 1)]
        popped = [i for i in range(1, n + 1)]
        for _ in range(100):
            random.shuffle(popped)
            if (Solution().validateStackSequence(pushed, popped) !=
                Solution().validateStackSequence2(n, popped)):
                print(
                    popped, 
                    Solution().validateStackSequence(pushed, popped),
                    Solution().validateStackSequence2(n, popped)
                    )

            """
            self.assertEqual(
                Solution().validateStackSequence([1,2,3,4,5], popped), 
                Solution().validateStackSequence2(5, popped),
                "Should be the same."
            )"""

if __name__ == "__main__":
    unittest.main()