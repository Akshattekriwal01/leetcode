"""
930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """
        two pointer: count number of subarrays that sums to at most S and S - 1
        """
        def atMost(k: int) -> int:
            window = l = 0
            cnt = 0
            for r, a in enumerate(A):
                window += a
                while l <= r and window > k:
                    window -= A[l]
                    l += 1
                cnt += r - l + 1
            return cnt

        return atMost(S) - atMost(S - 1)