import unittest

from sorting import MergeSort, QuickSort


class MergeSortTests(unittest.TestCase):
    def test_sort(self):
        a = list('MERGESORTEXAMPLE')
        sorter = MergeSort(a)
        sorter.sort()
        self.assertEqual(a, list('AEEEEGLMMOPRRSTX'))


class QuickSortTests(unittest.TestCase):
    def test_sort(self):
        a = list('QUICKSORTEXAMPLE')
        # a = list('KRATELEPUIMQCXOS')
        sorter = QuickSort()
        sorter.sort(a)
        self.assertEqual(a, list('ACEEIKLMOPQRSTUX'))
