"""
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:


    def bfs(self, root, target, k):
        parent = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ans = collections.deque([target])
        dist = 0
        while ans and dist < K:
            dist += 1
            for _ in range(len(ans)):
                node = ans.popleft()
                if node in parent:
                    ans.append(parent[node])
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
        return ans

