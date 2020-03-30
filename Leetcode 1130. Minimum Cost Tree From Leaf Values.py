"""
Given an array arr of positive integers, consider all binary trees such that:

    Each node has either 0 or 2 children;

    The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)

    The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4

"""
class Solution:
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        """
        dynamic programming
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)] # dp[i][j] = res by subarry arr[i...j]
        leafs = [[0] * n for _ in range(n)] # leafs[i][j] = max in arr[i...j]
        for i in range(n):
            dp[i][i] = 0
            leafs[i][i] = arr[i]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + leafs[i][k] * leafs[k+1][j] for k in range(i, j))
                leafs[i][j] = max(leafs[i][j-1], arr[j])
        return dp[0][n-1]

    def mctFromLeafValues2(self, arr: List[int]) -> int:
        """
        greedy
        """
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += arr[i] * min(arr[i-1:i] + arr[i+1:i+2])
            arr.pop(i)
        return res

    def mctFromLeafValues3(self, arr: List[int]) -> int:
        """
        monotonic decreasing stack
        """
        stack = []
        res = 0
        for num in arr:
            while stack and num >= stack[-1]:
                if len(stack) == 1 or num <= stack[-2]:
                    res += stack.pop() * num
                else:
                    res += stack.pop() * stack[-1]
            stack.append(num)
        while len(stack) > 1:
            res += stack.pop() * stack[-1]
        return res