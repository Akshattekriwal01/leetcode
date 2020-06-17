"""
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse(slow.next)
        p1 = dummy.next
        p2 = slow
        while p1 != p2:
            tmp = p2.next
            p2.next = p2.next.next
            tmp.next = p1.next
            p1.next = tmp
            p1 = p1.next.next
        return dummy.next

    def reverse(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p = head
        while p and p.next:
            new_head = p.next
            p.next = p.next.next
            new_head.next = dummy.next
            dummy.next = new_head
        return dummy.next