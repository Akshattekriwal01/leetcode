"""
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.
"""

import unittest
import heapq
import collections
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]],
        newEdges: List[List[int]]):
        """
        Prim's Algorithm
        """
        graph = collections.defaultdict(dict)
        for u, v in edges:
            graph[u][v] = 0
            graph[v][u] = 0
        for u, v, c in newEdges:
            graph[u][v] = c
            graph[v][u] = c

        mst = set()
        heap = [(0, 1)]
        min_cost = 0
        while heap:
            cost, u = heapq.heappop(heap)
            if u not in mst:
                min_cost += cost
                mst.add(u)
                for v, c in graph[u].items():
                    if v not in mst:
                        heapq.heappush(heap, (c, v))
        return min_cost


class TestSolution(unittest.TestCase):
    def test(self):
        n = 6
        edges = [[1, 4], [4, 5], [2, 3]]
        newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
        output = 7
        self.assertEqual(Solution().minCost(n, edges, newEdges), 
            output, "Should be 7")


if __name__ == "__main__":
    unittest.main()