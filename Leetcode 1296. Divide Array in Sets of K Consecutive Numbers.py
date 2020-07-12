"""
1296. Divide Array in Sets of K Consecutive Numbers
Medium

331

37

Add to List

Share
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/
"""

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """
        time: O(MlogM + N), M = number of unique numbers
        space: O(M)
        """
        n = len(nums)
        if n % k > 0:
            return False
        count = collections.Counter(nums)
        start = collections.deque() # number of subarray started as we process all numbers
        opened = 0 # number of all open subarray
        prev = -1
        for num in sorted(count):
            if opened > count[num] or (opened > 0 and num > prev + 1):
                return False
            start.append(count[num] - opened)
            prev, opened = num, count[num]
            if len(start) == k:
                opened -= start.popleft()
        return opened == 0