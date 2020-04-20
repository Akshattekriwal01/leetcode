"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.equal(s, t):
            return True
        if s and self.isSubtree(s.left, t):
            return True
        if s and self.isSubtree(s.right, t):
            return True
        return False

    def equal(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        else:
            return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)