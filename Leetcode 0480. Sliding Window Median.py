"""
480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.

"""

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi, median = [], [], []
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        for _ in range(k//2):
            heapq.heappush(hi, -heapq.heappop(lo))
        if k % 2 == 0:
            median.append(0.5 * (hi[0] - lo[0]))
        else:
            median.append(-lo[0])
        count = {}
        for i in range(k, len(nums)):
            in_num = nums[i]
            out_num = nums[i - k]
            count[out_num] = count.get(out_num, 0) + 1
            balance = 0
            if in_num <= -lo[0]:
                balance += 1
                heapq.heappush(lo, -in_num)
            else:
                balance -= 1
                heapq.heappush(hi, in_num)
            if out_num <= -lo[0]:
                balance -= 1
            else:
                balance += 1
            if balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            while len(lo) > 0 and count.get(-lo[0], 0) > 0:
                count[-heapq.heappop(lo)] -= 1
            while len(hi) > 0 and count.get(hi[0], 0) > 0:
                count[heapq.heappop(hi)] -= 1
            if k % 2 == 0:
                median.append(0.5 * (hi[0] - lo[0]))
            else:
                median.append(-lo[0])
        return median