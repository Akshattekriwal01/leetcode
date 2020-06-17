"""
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

class Solution:
    def findStrobogrammatic1(self, n: int) -> List[str]:
        """
        dynamic programming
        """
        if n == 0:
            return []
        rotation = [("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]
        if n % 2 == 0:
            ans = [""]
        else:
            ans = ["0", "1", "8"]
            n -= 1
        while n > 0:
            ans = [l + s + r for l, r in rotation for s in ans]
            n -= 2
        return [s for s in ans if len(s) == 1 or s[0] != "0"]

    def findStrobogrammatic1(self, n: int) -> List[str]:
        """ dfs """
        rotation = [("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]
        def dfs(s, ans):
            if len(s) == n:
                if len(s) == 1 or s[0] != "0":
                    ans.append(s)
                return
            for l, r in rotation:
                dfs(l + s + r, ans)
        ans = []
        if n % 2 == 0:
            dfs("", ans)
        else:
            dfs("0", ans)
            dfs("1", ans)
            dfs("8", ans)
        return ans