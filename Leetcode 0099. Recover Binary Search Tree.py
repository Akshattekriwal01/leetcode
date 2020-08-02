"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        def find_swapped(arr):
            x = y = -1
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    y = arr[i]
                    if x == -1:
                        x = arr[i-1]
                    else:
                        break
            return x, y

        def recover(node, count, vals):
            if node:
                if node.val in vals:
                    if node.val == vals[0]:
                        node.val = vals[1]
                    else:
                        node.val = vals[0]
                    count -= 1
                    if count == 0: return
                recover(node.left, count, vals)
                recover(node.right, count, vals)
        
        vals = find_swapped(inorder(root))
        recover(root, 2, vals)

    def recoverTree(self, root: TreeNode) -> None:
        stack = []
        node = root
        x = y = pred = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pred and node.val < pred.val:
                y = node
                if x is None:
                    x = pred
                else:
                    break
            predecessor = node
            node = node.right
        x.val, y.val = y.val, x.val

    def recoverTree(self, root: TreeNode) -> None:
        """ morris traversal """
        x = y = pred = None
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    if pred and node.val < pred.val:
                        y = node
                        if x == None:
                            x = pred
                    pred = node
                    node = node.right
            else:
                if pred and node.val < pred.val:
                    y = node
                    if x == None:
                        x = pred
                pred = node
                node = node.right
        x.val, y.val = y.val, x.val