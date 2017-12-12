class MaxHeap:
    def __init__(self, keys=[]):
        self._size = 0
        for key in keys:
            self.insert(key)

    def is_empty(self):
        return self._size == 0

    def size(self):
        pass

    def insert(self, value):
        self._size += 1

    def del_max(self):
        pass

    def _less(self, i, j):
        pass

    def _exchange(self, i, j):
        pass

    def _swim(self, k):
        pass

    def _sink(self, k):
        pass