"""
375. Guess Number Higher or Lower II
Medium

793

1244

Add to List

Share
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

"""

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """ 
        intuition: we want to find out the minimum cost to gurantee a win. Initially we only
        know that the secret number is within 1 to n; as we progress in the game, the lower
        and higher bound of the secrete number is getting smaller and smaller. Without lose
        generality, let's assume we want to find the minimum money required to win a game in
        the range of [lo, hi], and the objective is f(lo, hi).

        Because the secret can be any number in the range [lo, hi], we have to choose a guess
        to narrow it down. Let's say we change lo <= x <= hi as guess, to gurantee a win, we
        have to assume that this guess is wrong and the secret is either in range [lo, x-1] or
        [x+1, hi] with cost f(lo, x-1) and f(x+1, hi); in worst scenario, the secret will end
        in the side that cost more. So, f(lo, hi) = x + max(f(lo, x-1), f(x+1, hi)). Finally,
        we are smart enough to make a strategy to minimize f(lo, hi) by carefully choosing x.
        To do so, we can iterate through all x in range [lo, hi] and find the loswest cost x.

        So, finally f(lo, hi) = min(x + max(f(lo, x-1), f(x+1,hi))) for all x.

        top down
        dp[lo, hi] = mininum money to win if answer is between lo and hi (inclusive)
        """
        def dp(lo, hi, memo):
            if lo >= hi:
                return 0
            if (lo, hi) not in memo:
                ans = float("inf")
                for x in range(lo, hi + 1):
                    # max means to take the worst scenario
                    # min to minimize cost
                    ans = min(ans, x + max(dp(lo, x - 1, memo), dp(x + 1, hi, memo)))
                memo[(lo, hi)] = ans
            return memo[(lo, hi)]

        return dp(1, n, {})

    def getMoneyAmount(self, n: int) -> int:
        """ 
        bottom up 
        dp[i][j] = save as above
        """
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 0 # if i == j, we can win the game with no additional cost
        for d in range(2, n + 1):
            # d == length of window
            for i in range(1, n - d + 1):
                # i: start of a window
                # j: end of a window
                j = i + d
                cost = float("inf")
                for x in range(i, j + 1):
                    # x: number to guess
                    if x == i:
                        cost = min(cost, x + dp[x+1][j])
                    elif x == j:
                        cost = min(cost, x + dp[i][x-1])
                    else:   
                        cost = min(cost, x + max(dp[i][x-1], dp[x+1][j]))
                dp[i][j] = cost
        return dp[1][n]