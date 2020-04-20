"""
1135. Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
 

Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
"""

"""Minimum Spanning Tree

Kruskal’s Algorithm: 
    1. Sort edges by weight
    2. Add edge from lowest weight to highest
    3. Only add an edge if it will not create cycle

"""

class Solution:
    def minimumCost1(self, N: int, connections: List[List[int]]) -> int:
        """
        Kruskal’s Algorithm: 
            1. Sort edges by weight
            2. Add edge from lowest weight to highest
            3. Only add an edge if it will not create cycle
        Time: O(ElogE + Elog*V)
        Space: O(V)
        """
        connections.sort(key=lambda e: e[2])
        uf = UnionFind(N)
        cost = 0
        for i, j, c in connections:
            root_i, root_j = uf.find(i), uf.find(j)
            if root_i != root_j:
                cost += c
                uf.union(i, j)
            if uf.components == 1:
                return cost

    def minimumCost2(self, N: int, connections: List[List[int]]) -> int:
        """
        Prim’s Algorithm also use Greedy approach to find the minimum spanning tree. In Prim’s Algorithm we grow the spanning tree from a starting position. Unlike an edge in Kruskal's, we add vertex to the growing spanning tree in Prim's.

        Algorithm Steps:
            1. Maintain two disjoint sets of vertices. One containing vertices that are in the growing spanning tree and other that are not in the growing spanning tree.
            2. Select the cheapest vertex that is connected to the growing spanning tree and is not in the growing spanning tree and add it into the growing spanning tree. This can be done using Priority Queues. Insert the vertices, that are connected to growing spanning tree, into the Priority Queue.
            3. Check for cycles. To do that, mark the nodes which have been already selected and insert only those nodes in the Priority Queue that are not marked.

        Time: O((E + V)logV)
        Space: O(V)
        """
        graph = collections.defaultdict(list)
        for u, v, c in connections:
            graph[u].append((c, v))
            graph[v].append((c, u))
        visited = [False] * (N + 1)
        heap = [(0, 1)]
        min_cost = 0
        while queue:
            cost, u = heapq.heappop(heap)
            if not visited[u]:
                visited[u] = True
                min_cost += cost
                for c, v in graph[u]:
                    if not visited[v]:
                        heapq.heappush(heap, (c, v))
        return min_cost if sum(visited) == N else -1

class UnionFind:
    def __init__(self, n: int) -> None:
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.components = n

    def find(self, i):
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
            return
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        self.components -= 1