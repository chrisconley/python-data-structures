import unittest

from queue import Queue


class QueueTests(unittest.TestCase):
    def test_enqueue_with_one(self):
        queue = Queue()

        queue.enqueue(3)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.size, 0)

        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.size, 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size, 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.size, 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size, 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.size, 0)
        queue.enqueue(3)
        self.assertEqual(queue.size, 1)