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

    @property
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        return node.size if node else 0


class _Node:
    def __init__(self, key, value, num_nodes):
        self.key = key
        self.value = value
        self.num_nodes = num_nodes
        self.left, self.right = None, None

    @property
    def size(self):
        return self.num_nodes