from collections import deque


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return _Node(key, value, 1)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.num_nodes = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            tmp = node
            node = self._min(tmp.right)
            node.right = self._delete_min(tmp.right)
            node.left = tmp.left
        node.num_nodes = self._size(node.left) + self._size(node.right) + 1
        return node

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.num_nodes = self._size(node.left) + self._size(node.right) + 1
        return node

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    @property
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        return node.size if node else 0

    def serialize(self):
        height = self.height
        queue = deque([(self.root, 0)])
        result = []
        while len(queue) > 0:
            parent, level = queue.popleft()
            ret = parent and parent.key
            if level == -1:
                result.append(parent)
                continue
            result.append(ret)
            if level != height-1:
                if parent.left is None:
                    queue.append((None, -1))
                else:
                    queue.append((parent.left, level+1))
                if parent.right is None:
                    queue.append((None, -1))
                else:
                    queue.append((parent.right, level+1))

        return result

    @property
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                return 1
            else:
                return 1 + max(self._height(node.left), self._height(node.right))
        else:
            return 0

class _Node:
    def __init__(self, key, value, num_nodes):
        self.key = key
        self.value = value
        self.num_nodes = num_nodes
        self.left, self.right = None, None

    @property
    def size(self):
        return self.num_nodes