"""
815. Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = [set(r) for r in routes]
        # if two route share a stop, they are connected
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if any(s in routes[j] for s in routes[i]):
                    graph[i].append(j)
                    graph[j].append(i)
        # target routes
        targets = set([i for i, r in enumerate(routes) if T in r])
        visited = set([i for i, r in enumerate(routes) if S in r])
        queue = collections.deque([i for i in visited])
        steps = 1
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i in targets:
                    return steps
                for j in graph[i]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
            steps += 1
        return -1