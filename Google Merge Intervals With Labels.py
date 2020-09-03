"""
Given a set of inputs which represents [from, to, comment] in google docs.
Transform the input with overlapping offsets & unique comments to non overlapping offsets and duplicate comments.

Example 1:

Input: 
(0, 3): A
(2, 4): B
(5, 6): C

Output:
(0, 2): [A]
(2, 3): [A, B]
(3, 4): [B]
(5, 6): [C]
Example 2:

Input:
(0, 3): A
(0, 3): B
(2, 4): C
(5, 6): D

Output:
(0, 2): [A, B]
(2, 3): [A, B, C]
(3, 4): [C]
(5, 6): [D]
"""
import unittest
from typing import List, Dict, Tuple
class Solution:
    def merge(self, intervals):
        OPEN, CLOSE = 1, -1
        events = []
        for start, end, label in intervals:
            events.append((start, OPEN, label))
            events.append((end, CLOSE, label))
        events.sort()

        output = {}
        active = set()
        prev = float("inf")
        for time, typ, label in events:
            if time > prev and len(active) > 0:
                output[(prev, time)] = sorted(active)
            if typ == OPEN:
                active.add(label)
            else:
                active.remove(label)
            prev = time

        return output


class TestSolution(unittest.TestCase):
    def test1(self):
        input = [[0, 3, "A"], [2, 4, "B"], [5, 6, "C"]]
        output = {(0, 2): ["A"], (2, 3): ["A", "B"], (3, 4): ["B"], (5, 6): ["C"]}
        self.assertEqual(Solution().merge(input), output, "Should equal.")

    def test2(self):
        input = [[0, 3, "A"], [0, 3, "B"], [2, 4, "C"], [5, 6, "D"]]
        output = {(0, 2): ["A", "B"], (2, 3): ["A", "B", "C"], (3, 4): ["C"], (5, 6): ["D"]}
        self.assertEqual(Solution().merge(input), output, "Should equal.")

    def test3(self):
        input = [[0, 3, "A"], [0, 3, "B"], [2, 4, "C"], [5, 6, "D"], [0, 3, "E"], [4, 6, "F"], [5, 7, "G"]]
        output = {(0, 2): ["A", "B", "E"], (2, 3): ["A", "B", "C", "E"], (3, 4): ["C"], (4, 5): ["F"], (5, 6): ["D", "F", "G"], (6, 7): ["G"]}
        self.assertEqual(Solution().merge(input), output, "Should equal.")


if __name__ == "__main__":
    unittest.main()