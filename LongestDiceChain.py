"""
给很多色子，每个色子有两面，如果两个色子的左面或者右面点数一样，就可以串起来比如1-4 1-6可以串成4-1-1-6可以掉头。 求最长能串起来的长度。
"""

import unittest
import collections
from typing import List

class Solution:
    def longestDiceChain(self, dices: List[List[int]]) -> int:
        nodes = set()
        graph = collections.defaultdict(list)
        for i, (l, r) in enumerate(dices):
            nodes.add(l)
            nodes.add(r)
            graph[l].append((i, r))
            graph[r].append((i, l))
        
        ans = 0
        for node in nodes:
            ans = max(ans, self.dfs(graph, node, 0, set()))
        return ans

    def dfs(self, graph, node, length, visited):
        max_len = length
        for edge, nei in graph[node]:
            if edge not in visited:
                visited.add(edge)
                max_len = max(max_len, self.dfs(graph, nei, length + 2, visited))
                visited.remove(edge)
        return max_len

class TestSolution(unittest.TestCase):
    def test1(self):
        input = [[1, 3], [3, 1], [1, 4], [3, 4]]
        output = 8
        self.assertEqual(Solution().longestDiceChain(input), output, "Should be 8.")

    def test2(self):
        input = [[5, 6], [1, 3], [2, 3], [1, 5], [1, 8], [8, 2], [11, 12]]
        output = 12
        self.assertEqual(Solution().longestDiceChain(input), output, "Should be 12.")

if __name__ == "__main__":
    unittest.main()    