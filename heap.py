class MaxHeap:
    def __init__(self, keys=[]):
        self._size = 0
        self._heap = [None]
        for key in keys:
            self.insert(key)

    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    def insert(self, value):
        self._size += 1
        self._heap.append(value)
        self._swim(self._size)

    def del_max(self):
        max_key = self._heap[1]
        self._exchange(1, self._size)
        self._size -= 1
        self._heap.pop()
        self._sink(1)
        return max_key

    def _less(self, i, j):
        return self._heap[i] < self._heap[j]

    def _exchange(self, i, j):
        key = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = key

    def _swim(self, k):
        while k > 1 and self._less(int(k/2), k):
            self._exchange(int(k/2), k)
            k = int(k/2)

    def _sink(self, k):
        while 2 * k <= self._size:
            j = 2 * k
            if j < self._size and self._less(j, j+1):
                j += 1
            if not self._less(k, j):
                break
            self._exchange(k, j)
            k = j
