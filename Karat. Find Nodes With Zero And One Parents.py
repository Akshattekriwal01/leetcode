"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

parentChildPairs = [  (1, 3), (2, 3), (3, 6), (5, 6),
                               (5, 7), (4, 5), (4, 8), (8, 10)  ]
Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.
findNodesWithZeroAndOneParents(parentChildPairs) =>
    [ [1, 2, 4],    // Individuals with zero parents
    [5, 7, 8, 10] // Individuals with exactly one parent ]
"""


import unittest
import collections
from typing import List

class Solution:
    def findNodesWithZeroAndOneParents(self, 
        parentChildPairs: List[List[int]]) -> List[List[int]]:
        indegree = {}
        for u, v in parentChildPairs:
            indegree[u] = indegree.get(u, 0)
            indegree[v] = indegree.get(v, 0) + 1
        zero = []
        one = []
        for u, cnt in indegree.items():
            if cnt == 0:
                zero.append(u)
            if cnt == 1:
                one.append(u)
        return [zero, one]

    def hasCommonAncestor(self, 
        parentChildPairs: List[List[int]], node1: int, node2: int) -> bool:
        ## circles
        graph = collections.defaultdict(list) # adj list: child -> parent
        for u, v in parentChildPairs:
            graph[v].append(u)
        ## dfs node1 to get all ancestors
        stack = [node1]
        ancestors = set()
        while stack:
            node = stack.pop()
            for parent in graph[node]:
                ancestors.add(parent)
                stack.append(parent)
        ## dfs node2 to check if any of node2's ancestor exist in node1's ancestor
        stack = [node2]
        while stack:
            node = stack.pop()
            for parent in graph[node]:
                if parent in ancestors:
                    return True
                stack.append(parent)
        return False

    def findEarliestAncestor(self, 
        parentChildPairs: List[List[int]], node: int) -> int:
        ## build graph, store as adjacent list (child -> parent)
        graph = collections.defaultdict(list)
        for parent, child in parentChildPairs:
            graph[child].append(parent)
        if len(graph[node]) == 0:
            return -1
        ## bfs layer by layer, if next layer is empty, return -1
        """
        2 -> 6, 7 -> 3

        1----->2----->3----->4----->5
               |      |
               |      | 
               6----->7----->8----->9

        1 -> 2 -> 3 -> 4 -> 5, 4 steps
        1 -> 2 -> 6 -> 7 -> 8 -> 9, 5 steps
        1 -> 2 -> 6 -> 7 -> 3 -> 4 -> 5, 6 steps
        
        multiple path from between two nodes
        """
        curr = [node]
        visited = set([node])
        while curr:
            _next = []
            for node in curr:
                for parent in graph[node]:
                    if parent not in visited:
                        visited.add(parent)
                        _next.append(parent)
            if len(_next) == 0:
                return curr[0]
            curr = _next
        return -1



class TestSolution(unittest.TestCase):
    def test(self):
        parentChildPairs = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], 
            [4, 5], [4, 8], [8, 10]]
        output = [[1, 2, 4], [5, 7, 8, 10]]
        self.assertEqual(
            Solution().findNodesWithZeroAndOneParents(parentChildPairs), 
            output, "Should be [[1, 2, 4], [5, 7, 8, 10]].")
        self.assertFalse(
            Solution().hasCommonAncestor(parentChildPairs, 3, 8), 
            "Should be False")
        self.assertTrue(
            Solution().hasCommonAncestor(parentChildPairs, 5, 8), 
            "Should be True")
        self.assertTrue(
            Solution().hasCommonAncestor(parentChildPairs, 6, 8), 
            "Should be True")
        self.assertFalse(
            Solution().hasCommonAncestor(parentChildPairs, 1, 3), 
            "Should be False")

    def test2(self):
        parentChildPairs = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], 
            [4, 5], [4, 8], [8, 10], [11, 2]]
        self.assertEqual(
            Solution().findEarliestAncestor(parentChildPairs, 8),
            4, "Should be 4")
        self.assertEqual(
            Solution().findEarliestAncestor(parentChildPairs, 7),
            4, "Should be 4")
        self.assertEqual(
            Solution().findEarliestAncestor(parentChildPairs, 6),
            11, "Should be 11")
        self.assertEqual(
            Solution().findEarliestAncestor(parentChildPairs, 1),
            -1, "Should be -1")
if __name__ == "__main__":
    unittest.main()