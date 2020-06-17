"""
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0 or carry > 0:
            val = carry
            if i >= 0:
                val += int(num1[i])
                i -= 1
            if j >= 0:
                val += int(num2[j])
                j -= 1
            res.append(str(val % 10))
            carry = val // 10
        return "".join(res[::-1])