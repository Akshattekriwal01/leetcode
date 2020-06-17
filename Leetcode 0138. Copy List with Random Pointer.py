"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList1(self, head: "Node") -> "Node":
        """
        memorization
        time: O(N)
        space: O(N)
        """
        memo = {}
        def get_copy(node):
            if not node:
                return None
            if node not in memo:
                memo[node] = Node(node.val)
            return memo[node]

        new_head = get_copy(node)
        p, p_copy = head, new_head
        while p:
            p_copy.next = get_node(p.next)
            p_copy.random = get_node(p.random)
            p = p.next
            p_copy = p_copy.next
        return new_head

    def copyRandomList2(self, head: "Node") -> "Node":
        """
        inter
        """
        if not head:
            return None
        p = head
        while p:
            p_copy = Node(p.val, p.next, None)
            p.next = p_copy
            p = p_copy.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        head_copy = head.next
        p = head
        while p:
            p_copy = p.next
            p.next = p.next.next
            if p.next:
                p_copy.next = p.next.next
            else:
                p_copy.next = None
            p = p.next
        return head_copy

