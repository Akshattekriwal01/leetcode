"""
837. New 21 Game

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
    	""" naive approach, O(KW), TLE
    	"""
    	dp = [1.0] + [0.0] * N
    	ans = 0.0
    	for i in range(K):
    		for j in range(1, W + 1):
    			if i + j < K:
    				dp[i + j] += dp[i] / W
    				"""
    				repeated computation:
    					dp[1] = dp[0] / W
    					dp[2] = dp[0] / W + dp[1] / W
    					dp[3] = dp[0] / W + dp[1] / W + dp[2] / W
    					...
    				"""
    			elif i + j <= N:
    				ans += dp[i] / W
    	return ans


    def new21Game(self, N: int, K: int, W: int) -> float:
    	dp = [1.0] + [0.0] * N # dp[i] = probability of getting i points
    	wSum = 1.0 # total probability of previous W points
    	for i in range(1, N + 1):
    		dp[i] = wSum / W
    		if i < K:
    			wSum += dp[i]
    		if i >= W:
    			wSum -= dp[i-W]
    	return sum(dp[K:])