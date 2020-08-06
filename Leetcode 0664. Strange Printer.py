"""
664. Strange Printer

There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.

"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        """ top down"""
        def dp(i, j, memo):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) not in memo:
                ans = float("inf")
                for k in range(i, j):
                    ans = min(ans, dp(i, k, memo) + dp(k + 1, j, memo) - int(s[i] == s[k+1]))
                memo[(i, j)] = ans
            return memo[(i, j)]
        return dp(0, len(s) - 1, {})

    def strangePrinter(self, s: str) -> int:
        """ bottom up """
        n = len(s)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2, n + 1): # l: length of substr 
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - int(s[i] == s[k+1]))
        return dp[0][n-1]

""" 
follow up
店面被问了这个题目：
给你一个m*n的目标矩阵，里面都是>0的正整数，同时给你一个操作，这个操作take 5个参数(x1,x2, y1, y2, v)，
可以把矩阵中x >= x1, x <= x2, y >= y1, y <= y2的矩形区域全部设置成v这个值。问从一个全0的m*n矩阵开始，
最少需要多少个这个样的操作才可以把这个全0矩阵变成目标矩阵，并且给出所有操作的5个参数
"""