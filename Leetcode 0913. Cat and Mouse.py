"""
913. Cat and Mouse

A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (ie. the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a draw.

 

Example 1:

Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0
 

Note:

3 <= graph.length <= 50
It is guaranteed that graph[1] is non-empty.
It is guaranteed that graph[2] contains a non-zero element. 
"""

class Solution:
    def catMouseGame1(self, graph: List[List[int]]) -> int:
        """
        top-down dynamic programming:
        the outcome of the winner depends on three variable: position of mouse, position of cat and whose turn to play
        """
        n = len(graph)
        def dfs(t, x, y, memo):
            if t == (2 * n - 1):
                return 0
            if x == 0:
                return 1
            if x == y:
                return 2
            if (t, x, y) not in memo:
                res = 0
                if t % 2 == 0: # mouse turn
                    outcomes = [dfs(t + 1, nei, y) for nei in graph[x]]
                    if any(o == 1 for o in outcomes):
                        res = 1
                    elif any(o == 0 for o in outcomes):
                        res = 0
                    else:
                        res = 2
                else:
                    outcomes = [dfs(t + 1, x, nei) for nei in graph[y] if nei != 0]
                    if any(o == 2 for o in outcomes):
                        res = 2
                    elif any(o == 0 for o in outcomes):
                        res = 0
                    else:
                        res = 1
                memo[(t, x, y)] = res
            return memo[(t, x, y)]
        return dfs(0, 1, 2, {})

    def catMouseGame2(self, graph: List[List[int]]) -> int:
        """
        bottom up
        """
        n = len(graph)
        dp = [[[0] * n for _ in range(n)] for t in range(2 * n)]
        for t in range(2 * n - 2, -1, -1):
            for x in range(n):
                for y in range(n):
                    if x == 0:
                        dp[t][x][y] = 1
                    elif x == y:
                        dp[t][x][y] = 2
                    else:
                        if t % 2 == 0:
                            if any(dp[t+1][nei][y] == 1 for nei in graph[x]):
                                dp[t][x][y] = 1
                            elif any(dp[t+1][nei][y] == 0 for nei in graph[x]):
                                dp[t][x][y] = 0
                            else:
                                dp[t][x][y] = 2
                        else:
                            if any(dp[t+1][x][nei] == 2 for nei in graph[y] if nei != 0):
                                dp[t][x][y] = 2
                            elif any(dp[t+1][x][nei] == 0 for nei in graph[y] if nei != 0):
                                dp[t][x][y] = 0
                            else:
                                dp[t][x][y] = 1
        return dp[0][1][2]