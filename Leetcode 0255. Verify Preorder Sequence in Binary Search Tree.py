"""
255. Verify Preorder Sequence in Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
"""

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        In BST, node.left.val < node.val < node.right.val, and the preorder 
        traversal will visit left child all the way to the leaf before visiting
        any right child. This traversal order will reflect in the preorder 
        array as a decreasing val subseq. If we see a val that's greater than
        its preceeding val then it means it's the right child of that preceeding
        node and all its children nodes should have values larger than it; we
        use a variable lower_bound to denote it. If any future val is smaller 
        than this value, then we can return False. The lower_bound should be 
        updated anytime we see a right branch.

        time/space O(N)
        """
        lower_bound = float("-inf")
        stack = []
        for val in preorder:
            if val < lower_bound:
                return False
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
            stack.append(val)
        return True

    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        The space can be reduced to O(1) using preorder array as stack.
        """
        lower_bound = float("-inf")
        i = 0
        for val in preorder:
            if val < lower_bound:
                return False
            while i > 0 and val > preorder[i - 1]:
                lower_bound = preorder[i - 1]
                i -= 1
            preorder[i] = val
            i += 1
        return True