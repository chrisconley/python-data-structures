import unittest

import btree


class BinarySearchTreeTests(unittest.TestCase):
    def test_size(self):
        tree = btree.BinarySearchTree()
        self.assertEqual(tree.size, 0)

        tree.root = btree._Node('A', '1', 1)
        self.assertEqual(tree.size, 1)

    def test_get_put(self):
        tree = btree.BinarySearchTree()
        for index, character in enumerate('SEARCHEXAMPLE'):
            tree.put(character, index)

        self.assertEqual(tree.get('A'), 8)
        self.assertEqual(tree.get('E'), 12)
        self.assertEqual(tree.get('X'), 7)
        self.assertEqual(tree.get('x'), None)

        self.assertEqual(tree.size, 10)

    def test_delete(self):
        pass
