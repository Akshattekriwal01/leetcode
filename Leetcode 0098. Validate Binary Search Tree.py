"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorder(root, float("-inf"), float("inf"))
        
    def recursion(self, root: TreeNode, lo: int, hi: int) -> bool:
        if not root:
            return True
        if root.val <= lo or root.val >= hi:
            return False 
        return self.dfs(root.left, lo, root.val) and self.dfs(root.right, root.val, hi)

    def iteration(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))
        return True

    def inorder_traversal(self, root: TreeNode) -> bool:
        inorder = float("-inf")
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    def morris(self, root: TreeNode) -> bool:
        inorder = float("-inf")
        while root:
            if not root.left:
                if root.val <= inorder:
                    return False
                inorder = root.val
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    if root.val <= inorder:
                        return False
                    inorder = root.val
                    predecessor.right = None
                    root = root.right
        return True