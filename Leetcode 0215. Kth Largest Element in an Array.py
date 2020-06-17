"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""

class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        sorting
        time: O(NlogN)
        space: space used for sorting
        """
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        priority queue (heap)
        time: O(NlogK)
        space: O(K)
        """
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """
        quick-select partitioning
        time: average ~ O(N), worst O(N^2)
        space: O(logN)
        """
        import random
        random.shuffle(nums)

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def quick_select(lo, hi, k):
            pivot = lo
            for i in range(lo, hi):
                if nums[i] <= nums[hi]:
                    swap(i, pivot)
                    pivot += 1
            swap(pivot, hi)
            cnt = hi - pivot + 1
            if cnt == k:
                return nums[pivot]
            elif cnt > k:
                return quick_select(pivot + 1, hi, k)
            else:
                return quick_select(lo, pivot - 1, k - cnt)

        return quick_select(0, len(nums) - 1, k)
