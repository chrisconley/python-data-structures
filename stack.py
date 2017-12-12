class ResizingArrayStack:
    def __init__(self):
        self._array = [None]
        self._size = 0
        pass

    def push(self, item):
        if self._size == len(self._array):
            self._resize(2 * len(self._array))
        self._array[self.size] = item
        self._size += 1
        pass

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
