"""
1265. Print Immutable Linked List in Reverse

You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.

 

Follow up:

Could you solve this problem in:

Constant space complexity?
Linear time complexity and less than linear space complexity?
 

Example 1:

Input: head = [1,2,3,4]
Output: [4,3,2,1]
Example 2:

Input: head = [0,-4,-1,3,-5]
Output: [-5,3,-1,-4,0]
Example 3:

Input: head = [-2,0,6,4,4,-6]
Output: [-6,4,4,6,0,-2]
 

Constraints:

The length of the linked list is between [1, 1000].
The value of each node in the linked list is between [-1000, 1000].
"""

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """ recursion, time O(N), space O(N) """
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()

    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """ iteration, time O(N), space O(N) """
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        while stack:
            stack.pop().printValue()
    
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """ brute force, time O(N^2), space O(1) """
        tail = None
        while head != tail:
            curr = head
            while curr.getNext() != tail:
                curr = curr.getNext()
            curr.printValue()
            tail = curr


    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """ 
        sqrt decomposition: use stack to store nodes at sqrt(size) interval
        time O(N), space O(sqrt(N))

        We can further improve the algorithm by using varing block_size t.
        The num_blocks = n^(1/t), each block would require O(n^(1-1/t)) space 
        for the stack or recursion. 
        """
        import math

        def getSize(head):
            size = 0
            while head:
                size += 1
                head = head.getNext()
            return size
        
        def blockPrint(head, size):
            if head and size:
                blockPrint(head.getNext(), size-1)
                head.printValue()

        def decomposePrint(head, size, t):
            num_blocks = math.ceil(size ** (1 / t))
            block_size = size // num_blocks
            blocks = getBlocks(head, size, block_size)
            if size % block_size != 0:
                if t == 2:
                    blockPrint(blocks.pop(), size % block_size)
                else:
                    decomposePrint(blocks.pop(), size % block_size, t - 1)
            while blocks:
                if t == 2:
                    blockPrint(blocks.pop(), block_size)
                else:
                    decomposePrint(blocks.pop(), block_size, t - 1)

        def getBlocks(head, size, block_size):
            num_blocks = math.ceil(size / block_size)
            blocks = []
            p = head
            for i in range(size):
                if i % block_size == 0:
                    blocks.append(p)
                p = p.getNext()
            return blocks 

        size = getSize(head)
        decomposePrint(head, size, 3)

    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """ divide and conquer """
        def getSize(head):
            size = 0
            while head is not None:
                size += 1
                head = head.getNext()
            return size

        def helper(head, size):
            if size == 1:
                head.printValue()
            if size > 1:
                mid = head
                for _ in range(size//2):
                    mid = mid.getNext()
                helper(mid, size - size // 2)
                helper(head, size // 2)
        
        size = getSize(head)
        helper(head, size)