"""
1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""

class SnapshotArray:
    def __init__(self, length: int):
        """
        self.arr[i] = [sid, val], snapshots of ith element
        Space O(N*K), N = length, K = # of snapshots
        """
        self.arr = [[[0, 0]] for _ in range(length)] 
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        """
        if not already snapped, update val of previous snapshot
        otherwise, cache the new snapshot with new val
        Time O(1)
        """
        if self.arr[index][-1][0] == self.sid:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.sid, val])

    def snap(self) -> int:
        """
        lazy snap: meaning only increment snap_id
        Time O(1)
        """
        self.sid += 1
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        binary search for snapped value corresponding to snap_id
        Time O(logK)
        """
        i = bisect.bisect_left(self.arr[index], [snap_id + 1]) - 1  
        return self.arr[index][i][1]