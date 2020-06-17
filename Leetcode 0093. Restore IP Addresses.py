"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        time: 3 * 3 * 3
        """
        ans = []
        self.backtrack(s, 0, [], ans)
        return ans

    def backtrack(self, s, i, path, ans):
        if i == len(s) and len(path) == 4:
            ans.append(".".join(path))
        if i >= len(s) or len(path) >= 4:
            return 
        for l in range(1, 4):
            if l > 1 and s[i] == "0":
                continue
            if 0 <= int(s[i:i + l]) <= 255:
                self.backtrack(s, i + l, path + [s[i: i + l]], ans)