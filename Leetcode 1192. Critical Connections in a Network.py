"""
1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""
import collections
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False for _ in range(n)]
        lowest = [i for i in range(n)]
        ans = []

        def dfs(curr, prev, rank):
            visited[curr] = True
            lowest[curr] = rank
            for nei in graph[curr]:
                if nei == prev: continue
                if not visited[nei]:
                    dfs(nei, curr, rank + 1)
                lowest[curr] = min(lowest[curr], lowest[nei])
                if lowest[nei] >= rank + 1:
                    ans.append([curr, nei])
        dfs(0, -1, 0)
        return ans