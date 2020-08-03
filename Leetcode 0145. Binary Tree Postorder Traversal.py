"""
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        stack = []
        while root or stack:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if stack and root.right == stack[-1]:
                right = stack.pop()
                stack.append(root)
                root = right
            else:
                postorder.append(root.val)
                root = None
        return postorder

    def morris(self, root: TreeNode) -> List[int]:
        def reverse(arr, lo, hi):
            while lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1
            
        postorder = []
        dummy = TreeNode(0)
        dummy.left = root
        node = dummy
        while node:
            if node.left is None:
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor = node.left
                    postorder.append(predecessor.val)
                    cnt = 1
                    while predecessor.right != node:
                        predecessor = predecessor.right
                        postorder.append(predecessor.val)
                        cnt += 1
                    reverse(postorder, len(postorder) - cnt, len(postorder) - 1)
                    predecessor.right = None
                    node = node.right
        dummy.left = None
        return postorder