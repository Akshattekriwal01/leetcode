"""
958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        bfs
        cnt: # of non null nodes after curr node in bfs
        """
        queue = collections.deque([root])
        cnt = 1 if root else 0
        while queue:
            node = queue.popleft()
            if node is None:
                return cnt == 0
            cnt -= 1
            queue.append(node.left)
            queue.append(node.right)
            cnt += 1 if node.left else 0
            cnt += 1 if node.right else 0
        return True

    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        deq = collections.deque([(root, 1)])
        cnt = 1
        largest_idx = 1
        while deq:
            node, idx = deq.popleft()
            largest_idx = max(largest_idx, idx)
            if node.left:
                cnt += 1
                deq.append((node.left, idx * 2))
            if node.right:
                cnt += 1
                deq.append((node.right, idx * 2 + 1))
        return largest_idx == cnt