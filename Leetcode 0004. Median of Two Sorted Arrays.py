"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMediaSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        binary search: search cutting points cut1 & cut2 in nums1 and nums2 so that cut1 + cut2 == (len(nums1) + len(nums2)) // 2 and nums1[cut1-1] <=
        nums2[cut2] and nums1[cut1] >= nums2[cut2-1]
        time: O(log(min(m, n)))
        space: O(1)
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMediaSortedArrays(nums2, nums1)
        if m == 0:
            return 0.5 * (nums2[(n - 1) // 2] + nums[n // 2])
        cut = (m + n) // 2
        lo, hi = 0, m # search space for cut1
        MIN, MAX = float("-inf"), float("inf")
        while True:
            cut1 = lo + (hi - lo) // 2
            cut2 = cut - cut1
            L1 = nums1[cut1 - 1] if cut1 > 0 else MIN
            R1 = nums1[cut1] if cut1 < m else MAX
            L2 = nums2[cut2 - 1] if cut2 > 0 else MIN
            R2 = nums2[cut2] if cut2 < n else MAX
            if L1 > R2:
                hi = cut1 - 1
            elif L2 > R1:
                lo = cut1 + 1
            else:
                if (m + n) % 2 == 1:
                    return 1.0 * min(R1, R2)
                else:
                    return 0.5 * (max(L1, L2) + min(R1, R2))

    def findMediaSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        search for kth element in the two arrays
        """
        m, n = len(nums1), len(nums2)
        i = j = k = 0
        while k < (m + n) // 2:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            elif i < m:
                i += 1
            else:
                j += 1
            k += 1
        L1 = nums1[i - 1] if i > 0 else float("-inf")
        R1 = nums1[i] if i < m else float("inf")
        L2 = nums2[j - 1] if j > 0 else flaot("-inf")
        R2 = nums2[j] if j < n else float("inf")
        if (m + n) % 2 == 1:
            return 1.0 * min(R1, R2)
        else:
            return 0.5 * (max(L1, L2) + min(R1, R2))