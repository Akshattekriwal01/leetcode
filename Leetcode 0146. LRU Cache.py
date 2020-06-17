"""
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLNode(0, 0)
        self.tail = DLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[node]
            self._move_to_front(node)
        else:
            node = DLNode(key, value)
            self._add_first(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                key = self._pop_oldest().key
                del self.cache[key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        self._remove(node)
        self._add_first(node)

    def _pop_oldest(self):
        oldest = self.tail.prev
        self._remove(oldest)
        return oldest

    def _add_first(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head


class DLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None