"""
729. My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""

import bisect

class MyCalendar:
    def __init__(self):
        self.events = []
    
    def book(self, start: int, end: int) -> bool:
        """
        brute force: check if there's overlap between any event 
        """
        for s, e in self.events:
            if s < end and e > start:
                return False
        self.events.append([start, end])
        return True
    
class MyCalendar:
    def __init__(self):
        self.event_start = []
        self.event_end = []

    def book(self, start: int, end: int) -> bool:
        """ 
        binary search 
        """
        idx_start = bisect.bisect_left(self.event_end, start + 1)
        idx_end = bisect.bisect_right(self.event_start, end - 1) 
        if idx_start == idx_end:
            self.event_start = self.event_start[:idx_start] + [start] + self.event_start[idx_start:]
            self.event_end = self.event_end[:idx_end] + [end] + self.event_end[idx_end:]
        return idx_start == idx_end


class MyCalendar:
    """ binary search tree """
    def __init__(self):
        self.root = None
    
    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


class Node:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        else:
            return False