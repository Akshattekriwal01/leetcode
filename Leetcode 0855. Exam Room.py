"""
855. Exam Room

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

"""

class ExamRoom:
    def __init__(self, N: int):
        self.N = N
        self.heap = [Interval(-1, N, self.N)]

    def seat(self) -> int:
        itv = heapq.heappop(self.heap)
        if itv.x == -1:
            pos = 0
        elif itv.y == self.N:
            pos = self.N - 1
        else:
            pos = (itv.x + itv.y) // 2
        heapq.heappush(self.heap, Interval(pos, itv.y, self.N))
        heapq.heappush(self.heap, Interval(itv.x, pos, self.N))
        return pos

    def leave(self, p: int) -> None:
        head = tail = None
        for itv in self.heap:
            if itv.y == p:
                head = itv
            if itv.x == p:
                tail = itv
            if head and tail:
                break
        self.heap.remove(head)
        self.heap.remove(tail)
        self.heap.append(Interval(head.x, tail.y, self.N))
        heapq.heapify(self.heap)

class Interval:
    def __init__(self, x, y, N):
        self.x = x
        self.y = y
        self.d = self.dist(N)

    def dist(self, N):
        if self.x == -1:
            return self.y
        elif self.y == N:
            return N - 1 - self.x
        else:
            return (self.y - self.x) // 2

    def __lt__(self, interval):
        if self.d < interval.d:
            return False
        elif self.d > interval.d:
            return True
        elif self.x < interval.x:
            return True
        elif self.x > interval.x:
            return False
        else:
            return self.y < interval.y