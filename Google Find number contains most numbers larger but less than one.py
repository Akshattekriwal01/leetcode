"""
Q1:  input Array: [ 0.1, 0.2, 18.9, 17.5, 14.3, 12.1, 0.9,10.9] Output: 0.1

find X in Array, in the range [X, X+1) contains maximum numbers of the array.  

contains 3 numbers: 0.1, 0.2, 0.9…….[10.9, 11.9) contains 10.9...... return 0.1
"""

import collections
from typing import List

class Solution:
    def findNumber(self, nums: List[int]) -> float:
        nums.sort()
        deq = collections.deque()
        cnt = 0
        ans = None
        for x in nums:
            while deq and x - deq[0] >= 1.0:
                deq.popleft()
            deq.append(x)
            if len(deq) > cnt:
                ans = deq[0]
                cnt = len(deq)
        return ans