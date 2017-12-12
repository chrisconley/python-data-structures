import unittest

from heap import MaxHeap


class MaxHeapTests(unittest.TestCase):
    def test_is_empty(self):
        heap = MaxHeap()
        self.assertTrue(heap.is_empty())

        heap = MaxHeap([1, 2])
        self.assertFalse(heap.is_empty())
