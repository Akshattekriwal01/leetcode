"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        binary search
        bisect.bisect_left(arr, x): index of smallest element no less than x
        bisect.biset_right(arr, x): index of smallest element greater tnan x
        bisect.bisect_left(arr, x): number of elements less than x
        bisect.bisect_right(arr, x): number of elements less than or equal to x
        """
        import bisect
        lis = []
        for num in nums:
            if not lis or num > lis[-1]:
                lis.append(num)
            else:
                i = bisect.bisect_left(lis, num)
                lis[i] = num
        return len(lis)
