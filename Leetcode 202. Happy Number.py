"""
202. Happy Number
Easy

1723

372

Add to List

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        cycle detection in link list
        """
        slow = fast = n
        while True:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False

    def get_next(self, x):
        ans = 0
        while x > 0:
            ans += (x % 10) ** 2
            x //= 10
        return ans

