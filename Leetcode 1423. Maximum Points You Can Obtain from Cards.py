"""
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def dp(l, r, k, memo):
            """ time & space: O(N^2) TLE """
            if k == 1:
                return max(cardPoints[l], cardPoints[r])
            if (l, r, k) not in memo:
                memo[(l, r, k)] = max(
                    cardPoints[l] + dp(l + 1, r, k - 1, memo), 
                    cardPoints[r] + dp(l, r - 1, k - 1, memo))
            return memo[(l, r, k)]
        return dp(0, len(cardPoints) - 1, k, {})

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        """ 
        sliding window O(K) 
        [1,79,80,1,1,1,200,1]
                 l         r
               l        r
            l        r
         l         r 
         
        window (l, r): cards that are not used, fixed size n - k, r - l + 1 = n - k
                       initially, l = k, r = n - 1
        score: total score outside the window (l, r), result is max(score) as we move the window
                initally equals to sum(cardPoints[0:k])
        moving the window from right to left:
            at each iteration, we move the window towards left, 
                subtract the point at the new left boundary
                add the point at the previous right boundary
        """
        n = len(cardPoints)
        best = score = sum(cardPoints[:k])
        for l in range(k - 1, -1, -1):
            r = l + n - k
            score += cardPoints[r] - cardPoints[l]
            best = max(best, score)
        return best