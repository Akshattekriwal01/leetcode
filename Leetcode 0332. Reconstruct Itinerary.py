"""
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

class Solution:
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        for src in graph:
            # if graph not balanced, one city dominates the flights N = E/2, O(NlogN)
            # average case, O(V*NlogN), N = E / 2*V, so O(V* E/2V * log(E/2V)) ~ O(ElogE/V)
            graph[src].sort(reverse=True) 

        stack = ["JFK"]
        res = []
        while stack: # O(E)
            src = stack[-1]
            if len(graph[src]) > 0:
                stack.append(graph[src].pop())
            else:
                res.append(stack.pop())
        return res[::-1]


    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        for city in graph:
            graph[city].sort()
            visited[city] = [False] * len(graph[city])
        ans = []
        self.backtrack(len(tickets), graph, visited, "JFK", ["JFK"], ans)
        return ans

    def backtrack(self, n, graph, visited, dep, route, ans):
        if n == len(route):
            ans = route[:]
            return True
        for i, des in enumerate(graph[dep]):
            if not visited[dep][i]:
                visited[dep][i] = True
                route.append(des)
                if self.backtrack(n, graph, visited, des, route, ans):
                    return True
                visited[dep][i] = False
                route.pop()
        return False
