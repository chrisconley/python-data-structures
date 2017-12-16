import random


class MergeSort:
    def __init__(self, a):
        self.orig = a
        self.aux = [None] * len(a)

    def sort(self):
        self._sort(self.orig, 0, len(self.orig) - 1)

    def _sort(self, a, lo, hi):
        if hi <= lo:
            return
        mid = lo + int((hi - lo) / 2)
        self._sort(a, lo, mid)
        self._sort(a, mid+1, hi)
        self._merge(a, lo, mid, hi)

    def _merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi+1):
            self.aux[k] = a[k]
        for k in range(lo, hi+1):
            if i > mid:
                # exhausted left so take from right
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                # exhausted right so take from left
                a[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                # right key is less, so take it
                a[k] = self.aux[j]
                j += 1
            else:
                # left key is less or equal, so take it
                a[k] = self.aux[i]
                i += 1


class QuickSort:
    def __init__(self):
        pass

    def sort(self, a):
        random.shuffle(a)
        self._sort(a, 0, len(a) - 1)

    def _sort(self, a, lo, hi):
        if hi <= lo:
            return
        j = self._partition(a, lo, hi)
        self._sort(a, lo, j-1)
        self._sort(a, j+1, hi)

    def _partition(self, a, lo, hi):
        i = lo
        j = hi
        v = a[lo]
        while True:
            while a[i] <= v:
                i += 1
                if i == hi:
                    break
            while v <= a[j]:
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            self._exch(a, i, j)
        self._exch(a, lo, j)
        return j

    def _exch(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
