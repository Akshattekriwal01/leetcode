"""
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""

from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        delays = [float("inf") for _ in range(N + 1)]
        heap = [(0, K)]
        seen = set()
        while heap:
            time, u = heapq.heappop(heap)
            if u not in seen:
                seen.add(u)
                delays[u] = time
                for v, w in graph[u]:
                    if v not in seen:
                        heapq.heappush(heap, (time + w, v))
        max_delays = max(delays[1:])
        return max_delays if max_delays != float("inf") else -1