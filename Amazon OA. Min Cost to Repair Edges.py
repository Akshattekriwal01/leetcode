"""
There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes connected by an edge.
edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).
Example 1:

Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.
Example 2:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 410
Example 3:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 79
"""

import unittest
import collections
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]], 
        edgesToRepair: List[List[int]]) -> int:
        broken = set([(u, v) for u, v, _ in edgesToRepair])
        uf = UnionFind(n)
        components = n
        min_cost = 0
        for u, v in edges:
            if (u, v) in broken: continue
            if uf.union(u-1, v-1):
                components -= 1
            if components == 1:
                return min_cost
        edgesToRepair.sort(key=lambda e: e[2])
        for u, v, c in edgesToRepair:
            if uf.union(u-1, v-1):
                min_cost += c
                components -= 1
            if components == 1:
                return min_cost
        return -1

class UnionFind:
    def __init__(self, n: int) -> None:
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, i: int) -> int:
        root = i
        while root != self.id[root]:
            root = self.id[root]
        while i != root:
            j = self.id[i]
            self.id[i] = root
            i = j
        return root

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        return True 


class TestSolution(unittest.TestCase):
    def test1(self) -> None:
        n = 5
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
        output = 20
        self.assertEqual(Solution().minCost(n, edges, edgesToRepair), output,
            "Should be 20")

    def test2(self) -> None:
        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
        edgesToRepair = [[1, 6, 410], [2, 4, 800]]
        output = 410
        self.assertEqual(Solution().minCost(n, edges, edgesToRepair), output,
            "Should be 410")

    def test3(self) -> None:
        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
        edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
        output = 79
        self.assertEqual(Solution().minCost(n, edges, edgesToRepair), output,
            "Should be 79")


if __name__ == "__main__":
    unittest.main()