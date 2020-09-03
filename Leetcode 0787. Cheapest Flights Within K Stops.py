"""
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""


"""
Shortest path problem in graph:
    1. directed vs undirected
    2. weighted vs unweighted
    3. cyclic vs acyclic

Common templates:
    unweighted graph: bfs
    weighted graph with non-negative weight: Dijsktra's
    negative weight graph: Bellman Ford's

"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        time: O(K(E+V)logKV) ~ O(V^3logV)
        space: O(KV) ~ O(V^2)
        """
        import collections
        import heapq
        graph = collections.defaultdict(list)
        for from_city, to_city, cost in flights:
            graph[from_city].append((to_city, cost))

        heap = [(0, src, 0)] # (cost, city, num_flights)
        while heap:
            cost, city, num_flights = heapq.heappop(heap)
            if city == dst:
                return cost
            if num_flights <= K:
                for to_city, c in graph[city]:
                    heapq.heappush(heap, (cost + c, to_city, num_flights + 1))
        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        time: O(KVE) ~ O(V^3)
        space: O(KV + K) ~ O(V^2), first time is for memo space and second term is for stack space
        """
        graph = collections.defaultdict(list)
        for from_city, to_city, cost in flights:
            graph[to_city].append((from_city, cost))

        def dp(c, k, memo):
            if k < 0:
                return float("inf")
            if c == src:
                return 0
            if (c, k) not in memo:
                ans = float("inf")
                for from_city, cost in graph[c]:
                    ans = min(ans, cost + dp(from_city, k - 1, memo))
                memo[(c, k)] = ans
            return memo[(c, k)]

        min_cost = dp(dst, K + 1, {})
        if min_cost != float("inf"):
            return min_cost
        else:
            return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Bellman Ford's algorithm
        """
