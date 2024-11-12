class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self, root):
        self.root = root
        return
    
    def insert(self, node):
        if self.root is None:
            self.root = Node(node)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = Node(node)        