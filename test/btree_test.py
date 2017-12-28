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
        tree = btree.BinarySearchTree()
        for index, character in enumerate('SEARCHEXAMPLE'):
            tree.put(character, index)

        tree.delete('E')
        self.assertEqual(tree.root.left.key, 'H')

        self.assertEqual(tree.size, 9)

        self.assertEqual(tree.root.key, 'S')
        tree.delete('S')
        self.assertEqual(tree.root.key, 'X')
        self.assertEqual(tree.size, 8)

        tree.delete('X')
        self.assertEqual(tree.root.key, 'H')
        self.assertEqual(tree.root.right.key, 'R')
        self.assertEqual(tree.root.left.key, 'A')
        self.assertEqual(tree.size, 7)

    def test_serialize(self):
        tree = btree.BinarySearchTree()
        for index, character in enumerate('HCSAE'):
            tree.put(character, index)

        self.assertEqual(tree.serliaze(), ['H', 'C', 'S', 'A', 'E', None, None])

        tree = btree.BinarySearchTree()
        for index, character in enumerate('HCSAEX'):
            tree.put(character, index)

        self.assertEqual(tree.serliaze(), ['H', 'C', 'S', 'A', 'E', None, 'X'])

        tree = btree.BinarySearchTree()
        for index, character in enumerate('HCSAERX'):
            tree.put(character, index)

        self.assertEqual(tree.serliaze(), ['H', 'C', 'S', 'A', 'E', 'R', 'X'])

        tree = btree.BinarySearchTree()
        for index, character in enumerate('HCSAX'):
            tree.put(character, index)

        self.assertEqual(tree.serliaze(), ['H', 'C', 'S', 'A', None, None, 'X'])

        tree = btree.BinarySearchTree()
        for index, character in enumerate('HCSBXAY'):
            tree.put(character, index)

        self.assertEqual(tree.serliaze(), ['H', 'C', 'S', 'B', None, None, 'X', 'A', None, None, 'Y'])

    def test_height(self):
        tree = btree.BinarySearchTree()
        for index, character in enumerate('SEARCHEXAMPLE'):
            tree.put(character, index)

        self.assertEqual(tree.height, 6)
