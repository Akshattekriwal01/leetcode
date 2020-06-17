"""
410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

class Solution:
    def splitArray1(self, nums: List[int], m: int) -> int:
        """
        binary search
        """
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cnt = 0
            curr = 0
            for num in nums:
                if curr + num <= mid:
                    curr += num
                else:
                    cnt += 1
                    curr = num
            if cnt >= m:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def splitArray2(self, nums: List[int], m: int) -> int:
        """
        dynamic programming: define dp[i][j] as minimum largest subarray sum for splitting nums[0..j] in i parts
        
        time: O(MN^2)
        space: O(MN)
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        n = len(nums)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            dp[1][j] = prefix[j] - prefix[0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(j - 1, 0, -1):
                    dp[i][j] = min(dp[i][j], 
                        max(dp[i-1][k], prefix[j] - prefix[k]))
                    if prefix[i] - prefix[k] >= dp[i-1][k-1]:
                        break
        return dp[m][n]