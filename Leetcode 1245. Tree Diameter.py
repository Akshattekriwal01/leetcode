"""
1245. Tree Diameter

Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""

class Solution:
    def treeDiameter1(self, edges: List[List[int]]) -> int:
        """
        topological sort & bfs
        """
        if not edges:
            return 0
        graph = collections.defaultdict(list)
        indegree = [-1] * (len(edges) + 1)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            indegree[i] += 1
            indegree[j] += 1
        curr_layer = [i for i, d in enumerate(indegree) if d == 0]
        diameter = 0
        while len(curr_layer) > 1:
            next_layer = []
            for i in curr_layer:
                for j in graph[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        next_layer.append(j)
            if next_layer:
                diameter += 2
            else:
                diameter += 1
            curr_layer = next_layer
        return diameter

    def treeDiameter2(self, edges: List[List[int]]) -> int:
        """
        dfs
        """
        def dfs(node, parent, graph):
            maxDia = 0
            first, second = 0, 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                dia, dep = dfs(nei, node, graph)
                maxDia = max(maxDia, dia)
                if dep >= first:
                    second = first
                    first = dep
                elif dep >= second:
                    second = dep
            return max(maxDia, first + second), 1 + first
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return dfs(0, -1, graph)

    def treeDiameter3(self, edges: List[List[int]]) -> int:
        """
        bfs
        """
        def bfs(node, graph):
            leaf = None
            diameter = -1
            visited = set([node])
            queue = collections.deque([node])
            while queue:
                diameter += 1
                for _ in range(len(queue)):
                    leaf = queue.popleft()
                    for nei in graph[leaf]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            return leaf, diameter
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        leaf, _ = bfs(0, graph)
        return bfs(leaf, graph)[1]