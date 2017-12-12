import unittest

from stack import ResizingArrayStack


class ResizingArrayStackTests(unittest.TestCase):
    def test_is_empty(self):
        stack = ResizingArrayStack()
        self.assertTrue(stack.is_empty())

        stack = ResizingArrayStack()
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_size_after_push(self):
        stack = ResizingArrayStack()
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.size, 2)

    def test_pop_after_push(self):
        stack = ResizingArrayStack()
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)

    def test_size_after_pop(self):
        stack = ResizingArrayStack()
        stack.push(3)
        stack.push(4)
        stack.pop()
        self.assertEqual(stack.size, 1)

    def test_array_size(self):
        stack = ResizingArrayStack()
        for i in range(0, 9):
            stack.push(1)
        self.assertEqual(len(stack._array), 16)
        for i in range(0, 9):
            stack.pop()
        self.assertEqual(len(stack._array), 2)
