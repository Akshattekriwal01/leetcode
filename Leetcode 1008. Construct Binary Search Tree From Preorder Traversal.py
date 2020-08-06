"""
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            parent = stack[-1]
            while stack and val > parent.val:
                parent = stack.pop()
            if val < parent.val:
                parent.left = node
            else:
                parent.right = node
            stack.append(node)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(preorder, lower=float("-inf"), upper=float("inf")):
            if len(preorder) == 0 or preorder[0] < lower or preorder[0] > upper:
                return None
            val = preorder.popleft()
            root = TreeNode(val)
            root.left = helper(preorder, lower, val)
            root.right = helper(preorder, val, upper)
            return root
        
        return helper(collections.deque(preorder))