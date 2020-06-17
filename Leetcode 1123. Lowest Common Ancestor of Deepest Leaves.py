"""
1123. Lowest Common Ancestor of Deepest Leaves

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves1(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        parent = {}
        prev = [root]
        while prev:
            curr = []
            for node in prev:
                if node.left:
                    parent[node.left] = node
                    curr.append(node.left)
                if node.right:
                    parent[node.right] = node
                    curr.append(node.right)
            if len(curr) == 0:
                break
            prev = curr
        while prev:
            if len(prev) == 1:
                return prev[0]
            curr = set()
            for node in prev:
                curr.add(parent[node])
            if len(curr) == 1:
                return curr[0]
            prev = list(curr)

    def lcaDeepestLeaves2(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: 
                return 0, None
            left_height, left_lca = dfs(root.left)
            right_height, right_lca = dfs(root.right)
            if left_height == right_height:
                return 1 + left_height, root
            elif left_height > right_height:
                return 1 + left_height, left_lca
            else:
                return 1 + right_height, right_lca
        return dfs(root)[1]