import unittest

from heap import MaxHeap


class MaxHeapTests(unittest.TestCase):
    def test_is_empty(self):
        heap = MaxHeap()
        self.assertTrue(heap.is_empty())

        heap = MaxHeap([1, 2])
        self.assertFalse(heap.is_empty())

    def test_size_after_insertion(self):
        heap = MaxHeap([1, 2])
        heap.insert(3)
        heap.insert(4)
        self.assertEqual(heap.size, 4)

    def test_insert_and_del_max(self):
        heap = MaxHeap([1, 2])
        heap.insert(4)
        heap.insert(3)

        self.assertEqual(heap.size, 4)

        self.assertEqual(heap.del_max(), 4)
        self.assertEqual(heap.del_max(), 3)
        self.assertEqual(heap.del_max(), 2)
        self.assertEqual(heap.del_max(), 1)

    def test_insert_and_del_max_from_algs_book(self):
        heap = MaxHeap(['E', 'P', 'I', 'S', 'N', 'H', 'G', 'R', 'O', 'A'])
        heap.insert('T')

        self.assertEqual(heap.del_max(), 'T')
        self.assertEqual(heap.del_max(), 'S')
        self.assertEqual(heap.del_max(), 'R')
        self.assertEqual(heap.del_max(), 'P')
