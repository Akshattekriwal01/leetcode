class Solution:
    def exists(self, arr: List[int], k: int) -> bool:
        l, r = 0, len(arr) - 1
        while l + 1 <= r:
            if arr[l] + arr[r] == k:
                return True
            mid = l + (r - l) // 2
            if arr[mid] < k // 2:
                # for any i < mid, 2 * arr[i] < arr[mid] < k // 2
                # so arr[i] + arr[mid] < k // 4 + k // 2 < k
                l = mid + 1
            else:
                # if arr[mid] >= k // 2, arr[mid+1] > 2 * k // 2 >= k
                r = mid
        return False