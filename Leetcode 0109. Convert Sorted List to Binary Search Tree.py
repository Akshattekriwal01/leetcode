"""
109. Convert Sorted List to Binary Search Tree
Medium

2095

87

Add to List

Share
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None: return None
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next
        self.node = head
        return self.buildTree(0, n - 1)
        
    def buildTree(self, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        left = self.buildTree(start, mid - 1)
        root = TreeNode(self.node.val)
        self.node = self.node.next
        right = self.buildTree(mid + 1, end)
        root.left = left
        root.right = right
        return root