"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
Add a count attribute to the TreeNode class.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder

    def morris(self, root: TreeNode) -> List[int]:
        inorder = []
        node = root
        while node:
            if node.left is not None:
                predecessor = node.left
                while predecessor.right is not None and predecessor.right != node:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = node
                    node = node.left
                else:
                    inorder.append(node.val)
                    predecessor.right = None
                    node = node.right
            else:
                inorder.append(node.val)
                node = node.right        
        return inorder