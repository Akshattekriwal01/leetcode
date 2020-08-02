"""
144. Binary Tree Preorder Traversal
Medium

1590

59

Add to List

Share
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root,]
        preorder = []
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                preorder.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return preorder

    def morris(self, root: TreeNode) -> List[int]:
        preorder = []
        node = root
        while node:
            if not node.left:
                preorder.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    preorder.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return preorder