"""
Given two user's browser history, find the longest continuous common
history between user1 and user2.

Example: 

Input: [
    ["3234.html", "xys.html", "7hsaa.html"], 
    ["3234.html", ''sdhsfjdsh.html", "xys.html", "7hsaa.html"]
]

Output: ["xys.html", "7hsaa.html"]
"""

import unittest
from typing import List


class Solution:
    def longestCommonHistory(self, history: List[List[str]]) -> List[str]:
        maxLen = 0
        ans = []
        m, n = len(history[0]), len(history[1])
        # dp[i][j] = max len of common subarray between history[0][:i] and history[1][:j]
        # transition: dp[i][j] = dp[i-1][j-1] if history[0][i-1] == history[1][j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if history[0][i-1] == history[1][j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > maxLen: # update ans if find better one
                    maxLen = dp[i][j]
                    ans = history[0][i-maxLen:i]
        return ans
        for start in range(m):
            currLen = 0
            i = start
            for j in range(n):
                if i == m:
                    break
                if history[0][i] == history[1][j]:
                    currLen += 1
                else:
                    currLen = 0
                if currLen > maxLen:
                    maxLen = currLen
                    ans = history[1][j-currLen+1:j+1]
                i += 1
        for start in range(n):
            currLen = 0
            j = start
            for i in range(m):
                if j == n:
                    break
                if history[0][i] == history[1][j]:
                    currLen += 1
                else:
                    currLen = 0
                if currLen > maxLen:
                    maxLen = currLen
                    ans = history[0][i-currLen+1:j+1]
                j += 1

        return ans  


class TestSolution(unittest.TestCase):
    def test(self):
        history = [
            ["3234.html", "xys.html", "7hsaa.html"], 
            ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
        ]
        output = ["xys.html", "7hsaa.html"]
        self.assertEqual(Solution().longestCommonHistory(history), 
            output, "Should equal.")


if __name__ == "__main__":
    unittest.main()