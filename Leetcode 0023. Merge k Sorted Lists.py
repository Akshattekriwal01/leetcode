"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(NlogN)
# Space: O(N)
class Solution(object):
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        heap = [(l.val, i) for i, l in enumerate(lists) if l is not None]
        heapq.heapify(heap)
        p = dummy
        while heap:
            _, i = heapq.heappop(heap)
            node = p.next = lists[i]
            if node.next:
                lists[i] = node.next
                heapq.heappush(heap, (node.next.val, i))
            p = p.next
        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """
        divide and conquer: merge two list at once
        """
        def merge(l1, l2):
            dummy = ListNode(0)
            p, p1, p2 = dummy, l1, l2
            while p1 or p2:
                if p1 and p2:
                    if p1.val < p2.val:
                        p.next = p1
                        p1 = p1.next
                    else:
                        p.next = p2
                        p2 = p2.next
                elif p1:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2. next
                p = p.next
            return dummy.next

        if not lists: 
            return None

        d = 1
        while d < len(lists):
            for i in range(0, len(lists) - d, 2 * d):
                lists[i] = merge(lists[i], lists[i + d])
            d *= 2
        return lists[0]



class MyListNode(object):
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
