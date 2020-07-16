"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
Example 4:

Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.
Example 5:

Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        left: left[i] is min subarr len to the left of i
        right: right[i] is min subarr len to the right of i
        return min(left[i] + right[i + 1] for i: 0 to n  - 2)
        """
        n = len(arr)
        left = [float("inf") for _ in range(n)]
        right = [float("inf") for _ in range(n)]
        # build left
        presum = {0: -1}
        curr = 0
        for i in range(n):
            curr += arr[i]
            if i > 0:
                left[i] = left[i - 1]
            if curr - target in presum:
                left[i] = min(left[i], i - presum[curr - target])
            presum[curr] = i
        # build right
        presum = {0: n}
        curr = 0
        for i in range(n - 1, -1, -1):
            curr += arr[i] 
            if i < n - 1:
                right[i] = right[i + 1]
            if curr - target in presum:
                right[i] = min(right[i], presum[curr - target] - i)
            presum[curr] = i
        ans = min((left[i] + right[i + 1] for i in range(n - 1)), default=float("inf"))
        return ans if ans != float("inf") else -1


    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        dp[i] = min sub arr length up to idx i
        min_len_sum = running min sum of two sub array length
        """
        n = len(arr)
        dp = [float("inf") for i in range(n)]
        presum = {0: -1}
        curr = 0
        min_len_sum = float("inf")
        for r in range(n):
            curr += arr[r]
            if r > 0:
                dp[r] = dp[r - 1]
            if curr - target in presum:
                l = presum[curr - target]
                dp[r] = min(dp[r], r - l)
                if l >= 0:
                    min_len_sum = min(min_len_sum, dp[l] + r - l)
            presum[curr] = r
        return min_len_sum if min_len_sum != float("inf") else -1