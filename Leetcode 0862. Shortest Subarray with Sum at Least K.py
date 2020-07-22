"""
862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
"""

class Solution:
    def shortestSubArray(self, A: List[int], K: int) -> int: 
        """
        Monotonic queue: iterate the array and calculate prefix sum
            1. when the prefix sum is less than or equal to previous one, the
               previous should be popped out because the current one would result
               in a shorter subarray if such subarray exists.
            
            2. start from the front of the queue, if any prefix sum satisfies 
               prefix[j] - prefix[i] >= K, update the length and discard it 
               because a future prefix sum would only increase the length.
        """
        import collections
        queue = collections.deque([(0, -1)])
        curr = 0
        res = float("inf")
        for i, a in enumerate(A):
            curr += a
            while queue and queue[-1][0] >= curr:
                queue.pop()
            while queue and curr - queue[0][0] >= K:
                res = min(res, i - queue.popleft()[1])
            queue.append((curr, i))
        return res if res != float("inf") else -1
