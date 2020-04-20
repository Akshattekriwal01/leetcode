"""
Alice lives on a lattice. The lattice consists of points that have integer
coordinates. 

One day Alice decided she wants to go for a walk. She starts at lattice point A
and goes straight to lattice point B. After reaching B, she turns 90 degrees to
the right and moves straight in that direction. What is the first lattice point
that Alice will reach after the turn?

The points A and B have coordinates (AX, AY) and (BX, BY) respectively. You can assume that A and B are distinct.

Write a function:
    class Solution { public String solution(int AX, int AY, int BX, int BY); }
that, given four integers AX, AY, BX and BY, finds the coordinates of the first
lattice point that Alice will reach after turning right. It must return a 
string with two coordinates separated with a comma, without any spaces.

For example, given:
    AX = -1
    AY = 3
    BX = 3
    BY = 1
the function should return "2,-1".

"""

import unittest

class Solution:
    def latticePoint(self, AX: int, AY: int, BX: int, BY: int) -> str:
        def gcd(x, y):
            if x == 0:
                return y
            return gcd(y % x, x)

        dx, dy = BX - AX, BY - AY
        d = gcd(abs(dx), abs(dy))
        dx, dy = dx // d, dy // d
        CX, CY = BX + dy, BY - dx
        
        return "{},{}".format(CX, CY)

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().latticePoint(-1, 3, 3, 1), "2,-1", 
            "Should be 2,-1")

    def test2(self):
        self.assertEqual(Solution().latticePoint(0, 1, 0, 7), "1,7", 
            "Should be 1,7")

    def test3(self):
        self.assertEqual(Solution().latticePoint(1, 0, 7, 0), "7,-1", 
            "Should be 7,-1")

    def test4(self):
        self.assertEqual(Solution().latticePoint(0, 7, 0, 1), "-1,1",
            "Should be -1,1")

    def test5(self):
        self.assertEqual(Solution().latticePoint(7, 0, 1, 0), "1,1", 
            "Should be 1,1")

    def test6(self):
        self.assertEqual(Solution().latticePoint(7, 4, 1, 1), "0,3", 
            "Should be 0,3")

if __name__ == "__main__":
    unittest.main()
