"""
689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        greedy: for given middle interval, find the maximum left and right intervals; to achieve sum of the three intervals, moving the middle itervals and 
        """
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # left_dp:start index maximum left interval
        left_max = float("-inf")
        left_dp = [-1] * n
        for i in range(k, n + 1):
            if prefix[i] - prefix[i - k] > left_max:
                left_max = prefix[i] - prefix[i - k]
                left_dp[i - 1] = i - k
            else:
                left_dp[i - 1] = left_dp[i - 2] 
        # right: right[i] = start index of maximum right interval
        right_max = float("-inf")
        right_dp = [-1] * n
        for i in range(n - k, -1, -1):
            if prefix[i + k] - prefix[i] >= right_max:
                right_max = prefix[i + k] - prefix[i]
                right_dp[i] = i
            else:
                right_dp[i] = right_dp[i + 1]
        # iterate through middle interval and search for max
        ans = []
        curr_max = float("-inf")
        for i in range(k, n - 2 * k + 1):
            l = left_dp[i - 1]
            r = rigth_dp[i + k]
            tmp = 0
            tmp += prefix[l + k] - prefix[l]
            tmp += prefix[i + k] - prefix[i]
            tmp += prefix[r + k] - prefix[r]
            if tmp > curr_max:
                curr_max = tmp
                ans = [l, i, r]
        return ans


