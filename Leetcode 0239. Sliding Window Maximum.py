"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
"""

"""
Monotonic stack & queue summary

A common scenario of using a monotonic stack & queue is to greedy search an extreme value in an array, sometimes the extreme value may be confined in one end or both ends.

queue: if looking for extreme values about a window in an array, LC239 & LC862
stack: if looking for extreme values about the whole array, LC42 & LC84 & LC456 & LC1130 & LC1340

decreasing: if the greedy search involves local minimum in array, LC42 & LC456 & LC1130 & LC1340
increasing: if the greedy search involves local maximum in array, LC84 & LC239 & LC862
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        queue = collections.deque([])
        res = []
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i - queue[0] >= k - 1:
                queue.popleft()
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res


"""
Follow up: https://www.1point3acres.com/bbs/thread-621023-1-1.html

Given a array of integers, find the longest subarray, in which difference between any two numbers is less than or equal to D.
"""

class Solution:
    def longestSubarrayLength(self, nums: List[int], d: int) -> int:
        import collections
        res = 0
        desq = collections.deque([]) # descending queue
        ascq = collections.deque([]) # ascending queue
        left = 0
        for i, a in enumerate(nums):
            while desq and a > nums[desq[-1]]:
                desq.pop()
            while ascq and a < nums[ascq[-1]]:
                ascq.pop()
            desq.append(i)
            ascq.append(i)
            while nums[desq[0]] - nums[ascq[0]] > d:
                if desq[0] < ascq[0]:
                    left = max(left, desq.popleft() + 1)
                else:
                    left = max(left, ascq.popleft() + 1)
            res = max(res, i - left + 1)
        return res

    def longestSubarrayLength2(self, nums, d: int) -> int:
        import collections
        def exist(k):
            """
            check if there exist a subarray with length k of required conditions
            time: O(N)
            space: O(N)
            """
            desq = collections.deque([]) # descending queue
            ascq = collections.deque([]) # ascending queue
            for i, a in enumerate(nums):
                while desq and a > nums[desq[-1]]:
                    desq.pop()
                while ascq and a < nums[ascq[-1]]:
                    ascq.pop()
                desq.append(i)
                ascq.append(i)
                if desq[0] == i - k:
                    desq.popleft()
                if ascq[0] == i - k:
                    ascq.popleft()
                if i >= k - 1 and nums[desq[0]] - nums[ascq[0]] <= d:
                    return True
            return False

        lo, hi = 1, len(nums)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if exist(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

nums = [4, 8, 6, 5, 9, 7, 2, 3, 1]
for d in range(9):
    print(d, Solution().longestSubarrayLength(nums, d))