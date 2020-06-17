"""
1060. Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""

class Solution:
    def missingElement1(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] - 1 >= k:
                return nums[i - 1] + k
            k -= nums[i] - nums[i - 1] - 1
        return nums[-1] + k

    def missingElement2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        missing = lambda i: nums[i] - nums[0] - i
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        i = 0
        while k > missing(i):
            i += 1
        return nums[i - 1] + k - missing(i - 1)

    def missingElement3(self, nums: List[int], k: int) -> int:
        missing = lambda i: nums[i] - nums[0] - i
        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        # search for index such that missing(i - 1) < k <= missing(i)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if k > missing(mid):
                lo = mid + 1
            else:
                hi = mid
        return nums[lo - 1] + k  - missing(lo - 1)