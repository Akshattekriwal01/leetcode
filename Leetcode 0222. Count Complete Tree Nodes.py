"""
222. Count Complete Tree Nodes
Medium

2174

203

Add to List

Share
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """ borrow the indexing technique from binary heap tree, space/time O(N) """
        def dfs(node, index):
            if node.left and node.right:
                return max(dfs(node.left, 2 * index), dfs(node.right, 2 * index + 1))
            elif node.left:
                return dfs(node.left, 2 * index)
            else:
                return index
        if not root:
            return 0
        return dfs(root, 1)

    def countNodes(self, root: TreeNode) -> int:
        """ 
        binary search
            If we know the depth of the tree d, then the total number of nodes
            is (1 + 2 + 4 + ... + 2 ^ (d - 1)) + n (nodes in last layer).
            Now, the problem becomes finding the number n. We know that 
            1 <= n <= 2 ^ d, so we can binary search for n. 
        """
        if not root:
            return 0
        d = 0
        node = root
        while node.left:
            d += 1
            node = node.left
        
        lo, hi = 0, 2 ** d - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.exists(root, mid, d):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return 2 ** d - 1 + lo

    def exists(self, node, idx, depth):
        lo, hi = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = lo + (hi - lo) // 2
            if idx <= mid:
                node = node.left
                hi = mid
            else:
                node = node.right
                lo = mid + 1
        return node is not None