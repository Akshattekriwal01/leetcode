"""
Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same. There can be at max A 'a', B 'b' and C 'c'.

Example 1:

Input: A = 1, B = 1, C = 6
Output: "ccbccacc"
Example 2:

Input: A = 1, B = 2, C = 3
Output: "acbcbc"
"""

import unittest
import heapq

class Solution:
    def longestString(self, A: int, B: int, C: int) -> str:
        heap = [(-A, "a"), (-B, "b"), (-C, "c")]
        heapq.heapify(heap)
        res = []
        while heap:
            cnt1, char1 = heapq.heappop(heap)
            if len(res) > 1 and char1 == res[-1] == res[-2]:
                if heap:
                    cnt2, char2 = heapq.heappop(heap)
                    res.append(char2)
                    cnt2 += 1
                    heapq.heappush(heap, (cnt1, char1))
                    if cnt2 < 0:
                        heapq.heappush(heap, (cnt2, char2))
            else:
                res.append(char1)
                cnt1 += 1
                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, char1))
        return "".join(res)

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().longestString(1, 1, 6), "ccaccbcc",
            "Should be \"ccaccbcc\"")

    def test2(self):
        self.assertEqual(Solution().longestString(1, 2, 3), "cbcabc",
            "Should be \"cbcabc\"")


if __name__ == "__main__":
    unittest.main()