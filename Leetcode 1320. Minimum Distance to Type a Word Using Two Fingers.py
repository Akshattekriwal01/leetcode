"""
1320. Minimum Distance to Type a Word Using Two Fingers


You have a keyboard layout as shown above in the XY plane, where each English uppercase letter is located at some coordinate, for example, the letter A is located at coordinate (0,0), the letter B is located at coordinate (0,1), the letter P is located at coordinate (2,3) and the letter Z is located at coordinate (4,1).

Given the string word, return the minimum total distance to type such string using only two fingers. The distance between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|. 

Note that the initial positions of your two fingers are considered free so don't count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: 
Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: 
Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
Example 3:

Input: word = "NEW"
Output: 3
Example 4:

Input: word = "YEAR"
Output: 7
 

Constraints:

2 <= word.length <= 300
Each word[i] is an English uppercase letter.
"""

import collections


class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        2d dp
        state: (a, b) position of two fingers
        transition: (a, b) => (a, c) or (c, b)
        """
        def dist(i, j):
            if i == 26 or j == 26:
                return 0
            return abs(i // 6 - j // 6) + abs(i % 6 - j % 6)

        dp = {(26, 26): 0}
        for c in word:
            k = ord(c) - ord("A")
            tmp = collections.defaultdict(lambda: float("inf"))
            for i, j in dp:
                tmp[(i, k)] = min(tmp[(i, k)], dp[(i, j)] + dist(j, k))
                tmp[(k, j)] = min(tmp[(k, j)], dp[(i, j)] + dist(i, k))
            dp = tmp
        return min(dp.values())

    def minimumDistance(self, word: str) -> int:
        """
        intuition: naively the dp state depends on the positions of both
        finger. However, one finger always stays in previous letter in the 
        word, so at the ith letter, the state only depends on the position
        of the finger not on previous letter.

        dp[i] = min cost until previous letter with one hand at position i 
        and other hand 
        """
        def dist(i, j):
            if i == 26 or j == 26:
                return 0
            return abs(i // 6 - j // 6) + abs(i % 6 - j % 6)

        dp = [0] * 27
        prev = 26 # initially, the other finger on hover position
        for c in word:
            dp_new = [float("inf") for _ in range(27)]
            i = ord(c) - ord("A")
            # move the finger from prev position to current position
            for j in range(27):
                if j != prev:
                    # for this finger to stay at j, we have to move the other finger at previous letter to i
                    dp_new[j] = dp[j] + dist(prev, i)
                else:
                    # we have the freedom to move either fingers as long as one finger end up at j
                    dp_new[j] = min(dp[j] + dist(prev, i), min(dp[k] + dist(i, k) for k in range(27)))
            prev = i
            dp = dp_new
        return min(dp)