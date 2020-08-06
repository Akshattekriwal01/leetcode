"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = collections.deque(preorder)
        index_map = {val: idx for idx, val in enumerate(inorder)}

        def dfs(start, end):
            if start == end:
                return None
            val = preorder.popleft()
            idx = index_map[val]
            root = TreeNode(val)
            root.right = dfs(idx + 1, end)
            root.left = dfs(start, idx)
            return root
        
        return dfs(0, len(inorder))
            