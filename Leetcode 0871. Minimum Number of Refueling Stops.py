"""
871. Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """ 
        dynamic programming
        dp[i] = max fuel can collect with i stops

        At ith station, we check for j stops (j <= i), if the max fuel can
        reach station i; then max fuel of j + 1 stops can be updated with: 
        dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1]); finally, answer
        is given by the smallest # of stops for which dp[j] >= target.

        Time O(N^2), Space O(N)
        """
        n = len(stations)
        dp = [startFuel] + [0] * n
        for i in range(n):
            for s in range(i, -1, -1):
                if dp[s] >= stations[i][0]:
                    dp[s + 1] = max(dp[s + 1], dp[s] + stations[i][1])
        for i in range(n + 1):
            if dp[i] >= target:
                return i
        return -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """ 
        greedy: iteration the stations, and check if tank contains enough fuel 
        to reach the current station; if yes, we continue without refueling; if
        no, it means we need to go back to refuel at a previous station; and we
        should choose the station with maximum possible gas avaiable (use max heap).
        """
        import heapq

        if startFuel >= target: return 0
        refuels = 0
        tank = startFuel
        # store gases in previous stations that was not refueled
        # use negative values to minimic behavior of max heap
        max_heap = [] 
        for loc, gas in stations:
            while tank < loc:
                if len(max_heap) == 0: return -1
                tank -= heapq.heappop(max_heap)
                refuels += 1
                if tank >= target: return refuels
            heapq.heappush(max_heap, -gas) 

        while tank < target:
            if len(max_heap) == 0: return -1
            tank -= heapq.heappop(max_heap)
            refuels += 1
        return refuels



