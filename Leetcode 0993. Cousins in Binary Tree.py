"""
993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

"""

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [(root, 0)]
        seen = {}
        while stack:
            node, depth = stack.pop()
            if node.left and node.right:
                if sorted([node.left.val, node.right.val]) == sorted([x, y]):
                    return False
            seen[node.val] = depth
            if x in seen and y in seen:
                return seen[x] == seen[y]
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return False