"""
658. Find K Closest Elements

Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104
"""

class Solution:
    def findClosestElement1(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        greedy + binary search
        time: O(logN + k)
        space: O(1)
        """
        left = right = bisect.bisect_right(arr, x)
        while right - left < k:
            if left == 0:
                return arr[:k]
            elif right == len(arr):
                return arr[-k:]
            elif x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]

    def findClosestElement2(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]