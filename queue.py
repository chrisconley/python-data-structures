"""
LinkedList implementation from Section 1.3 pgs 150
"""


class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def enqueue(self, item):
        if self.size >= 1:
            # the old last is replaced with new item
            old_last = self._last
            node = Node(item, prev_item=old_last)
            old_last.next_item = node
            self._last = node
        elif self.size == 0:
            # no items, this item is both first and last
            node = Node(item)
            self._first = node
            self._last = node
        self._size += 1

    def dequeue(self):
        if self._size >= 2:
            old_first = self._first
            item = old_first.item
            self._first = old_first.next_item
        elif self.size == 1:
            item = self._first.item
            self._first = None
            self._last = None
        elif self.size == 0:
            raise Exception('Not allowed')
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size


class Node:
    def __init__(self, item, next_item=None, prev_item=None):
        self.item = item
        self.next_item = next_item
        self.prev_item = prev_item
