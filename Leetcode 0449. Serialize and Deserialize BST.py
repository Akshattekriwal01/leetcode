"""
449. Serialize and Deserialize BST
Medium

1330

70

Add to List

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
            if not root: return []
            return postorder(root.left) + postorder(root.right) + [root.val]
        return "".join([self.int_to_str(x) for x in postorder(root)])
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = [self.str_to_int(data[i:i+4]) for i in range(0, len(data), 4)]
        def buildTree(lower=float("-inf"), upper=float("inf")):
            if len(vals) == 0 or vals[0] < lower or vals[0] > upper:
                return None
            val = vals.pop()
            root = TreeNode(val)
            root.right = buildTree(val, upper)
            root.left = buildTree(lower, val)
            return root
        return buildTree()

    def int_to_str(self, n):
        chars = []
        for _ in range(4):
            chars.append(chr(n & 0xff))
            n >>= 8
        return "".join(chars[::-1])

    def str_to_int(self, s):
        num = 0
        for c in s:
            num = num * 256 + ord(c)
        return num

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))