"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        """
        add one by one
        """
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            val = carry
            if i >= 0:
                val += int(a[i])
                i -= 1
            if j >= 0:
                val += int(b[j])
                j -= 1
            carry = val >> 1
            res.append(str(val & 1))
        return "".join(res[::-1])

    def addBinary2(self, a: str, b: str) -> str:
        """
        facebook variation: no addtion operation
        """
        x = int(a, 2) # sum without carry
        y = int(b, 2) # carry shift left by 1
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]

