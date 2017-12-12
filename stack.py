"""
ResizingArrayStack and LinkedList Stack implementations from Section 1.3 pgs 136 and 147
"""


class ResizingArrayStack:
    def __init__(self):
        self._array = [None]
        self._size = 0

    def push(self, item):
        if self._size == len(self._array):
            self._resize(2 * len(self._array))
        self._array[self.size] = item
        self._size += 1

    def pop(self):
        value = self._array[self._size-1]
        self._array[self._size - 1] = None
        self._size -= 1
        if self._size > 0 and self._size == int(len(self._array)/4):
            self._resize(int(len(self._array)/2))
        return value

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, num):
        temp = [None] * num
        for i in range(0, self._size):
            temp[i] = self._array[i]
        self._array = temp


class Stack:
    def __init__(self):
        self._first = None
        self._size = 0

    def push(self, item):
        old_first = self._first
        self._first = Node(item, next_item=old_first)
        self._size += 1

    def pop(self):
        old_first = self._first
        self._first = old_first.next_item
        self._size -= 1
        return old_first.item

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        next_item = self._first
        while next_item is not None:
            yield next_item.item
            next_item = next_item.next_item


class Node:
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item
