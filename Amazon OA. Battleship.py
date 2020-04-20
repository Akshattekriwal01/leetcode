"""
Jack plays a game of battleships with his friend Stacy. The game is played on a square map of N
rows, numbered from 1 to N. Each row contains N cells, labeled with consecutive English upper-case
letters (A, B, C, etc.). Each cell is identified by a string composed of its row number followed by its
column number: for example, "9C" denotes the third cell in the 9th row, and "15D" denotes the
fourth cell in the 15th row.
Jack marks the positions of all his ships on the map (which is not shown to Stacy). Ships are defined
by rectangles with a maximum area of 4 cells. Stacy picks map cells to hit some ships. A ship is
considered to be hit if at least one of its constituent cells is hit. If all of a ship's cells are hit, the ship is
sunk.
The goal is to count the number of sunk ships and the number of ships that have been hit but not
sunk.
For example, the picture below shows a map of size N = 4 with two blue ships and five hits marked
with the letter 'X':

image

In this example, one ship has been sunk and the other has been hit but not sunk. In the next picture,
the sunken ship is shown in grey and the ship that has been hit but not yet sunk appears in red:

image

The positions of ships are given as a string S, containing pairs of positions describing respectively the
top-left and bottom-right corner cells of each ship. Ships' descriptions are separated with commas.
The positions of hits are given as a string T, containing positions describing the map cells that were
hit: for the map in the example shown above, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A". Ships in
S and hits in T may appear in any order.
Write a function:
class Solution { public String solution(int N, String S, String T); }
that, given the size of the map N and two strings S, T that describe the positions of ships and hits
respectively, returns a string with two numbers: the count of sunken ships and the count of ships that
have been hit but not sunk, separated with a comma.
For instance, given N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A", your function should return
"1,1", as explained above.
Given N = 3, S = "1A 1B,2C 2C" and T = "1B", your function should return "0,1", because one ship
was hit but not sunk.
The positions of ships are given as a string S, containing pairs of positions describing respectively the
top-left and bottom-right corner cells of each ship. Ships' descriptions are separated with commas.
The positions of hits are given as a string T, containing positions describing the map cells that were
hit: for the map in the example shown above, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A". Ships in
S and hits in T may appear in any order.
Write a function:

class Solution { public String solution(int N, String S, String T); }

that, given the size of the map N and two strings S, T that describe the positions of ships and hits
respectively, returns a string with two numbers: the count of sunken ships and the count of ships that
have been hit but not sunk, separated with a comma.

For instance, given N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A", your function should return
"1,1", as explained above.

Given N = 3, S = "1A 1B,2C 2C" and T = "1B", your function should return "0,1", because one ship
was hit but not sunk.

image

Given N = 12, S = "1A 2A,12A 12A" and T = "12A", your function should return "1,0", because one
ship was hit and sunk.
Assume that:

N is an integer within the range [1..26];
string S contains the descriptions of rectangular ships of area not greater than 4 cells;
there can be at most one ship located on any map cell (ships do not overlap);
each map cell can appear in string T at most once;
string S and string T contains only valid positions given in specified format.
In your solution, focus on correctness. The performance of your solution will not be the focus of the
assessment.
"""

import unittest
from typing import List

class Solution:
    def hitAndSunk(self, N: int, S: str, T: str) -> str:
        colnum = lambda c: ord(c) - ord("A") + 1
        positions = set([(int(p[:-1]), colnum(p[-1])) for p in T.split()])
        hit = sunk = 0
        for ship in S.split(","):
            tl, br = ship.split()
            t, l = int(tl[:-1]), colnum(tl[-1])
            b, r = int(br[:-1]), colnum(br[-1])
            area = (b - t + 1) * (r - l + 1)
            cnt = 0
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if (i, j) in positions:
                        cnt += 1
            if area == cnt:
                sunk += 1
            elif cnt > 0:
                hit += 1
        return "{},{}".format(sunk, hit)


class TestSolution(unittest.TestCase):
    def test1(self):
        N = 4
        S = "1B 2C,2D 4D"
        T = "2B 2D 3D 4D 4A"
        output = "1,1"
        self.assertEqual(Solution().hitAndSunk(N, S, T), output, 
            "Should be 1,1")

    def test2(self):
        N = 3
        S = "1A 1B,2C 2C" 
        T = "1B"
        output = "0,1"
        self.assertEqual(Solution().hitAndSunk(N, S, T), output, 
            "Should be 0,1")

    def test3(self):
        N = 12
        S = "1A 2A,12A 12A" 
        T = "12A"
        output = "1,0"
        self.assertEqual(Solution().hitAndSunk(N, S, T), output, 
            "Should be 1,0")


if __name__ == "__main__":
    unittest.main()