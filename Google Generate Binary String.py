"""
Q2. genrate a binary string which have  k 1, and the length is n. For example, if n = 4 and k = 2, the answer is:
'0011', '1100', '1010'.............
"""

class Solution:
    def generateStrings(self, n: int, k: int) -> List[str]:
        output = []
        self.dfs([], n, k, output)
        return output

    def dfs(self, path: List[str], n: int, k: int, output) -> None:
        if k == 0:
            output.append("".join(path) + "0" * n)
            return
        if n == k:
            output.append("".join(path) + "1" * n)
            return
        ## add one "0"
        path.append("0")
        self.dfs(path, n - 1, k, output)
        path.pop()
        ## add one "1"
        path.append("1")
        self.dfs(path, n, k - 1, output)
        path.pop()