"""
652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        hash2idx = {"0": 0} # null tree
        hash2node = {}
        hash2cnt = {}
        def dfs(node):
            if not node:
                return 0
            # unique identifier of a tree is "node.val,uid(left_subtree),uid(right_subtree)"
            uid = ",".join([str(node.val), str(dfs(node.left)), str(dfs(node.right))])
            if uid not in hash2idx:
                hash2idx[uid] = len(hash2idx)
                hash2node[uid] = node
                hash2cnt[uid] = 1
            else:
                hash2cnt[uid] += 1
            return hash2idx[uid]
        
        dfs(root)
        ans = []
        for uid in hash2cnt:
            if hash2cnt[uid] > 1:
                ans.append(hash2node[uid])
        return ans