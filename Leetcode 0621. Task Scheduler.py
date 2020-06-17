"""
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

class Solution:
    def leastInterval1(self, tasks: List[int], n: int) -> int:
        count = [-c for c in collections.Counter(tasks).values()]
        heapq.heapify(count)
        time = 0
        while count:
            tmp = []
            for i in range(n + 1):
                time += 1
                if count:
                    c = heapq.heappop(count)
                    if c + 1 < 0:
                        tmp.append(c + 1)
                if not count and not tmp:
                    break
            for c in tmp:
                heapq.heappush(count, c)
        return time

    def leastInterval2(self, tasks: List[int], n: int) -> int:
        count = [0] * 26
        for c in tasks:
            count[ord(c) - ord("A")] += 1
        count.sort()
        max_val = count[25] - 1
        idle = max_val * n
        for i in range(24, -1, -1):
            idle -= min(max_val, count[i])
        return len(tasks) + idle if idle > 0 else len(tasks)