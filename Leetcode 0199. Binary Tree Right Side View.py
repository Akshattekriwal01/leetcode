"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sideview = {}
        stack = [(root, 0)]
        H = -1
        while stack:
            node, depth = stack.pop()
            H = max(H, depth)
            if depth not in sideview:
                sideview[depth] = node.val
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return [sideview[h] for h in range(H + 1)]
