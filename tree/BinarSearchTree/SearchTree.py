class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)
        return
    
    def insert(self, nodeEl):
        if self.root is None:
            self.root = Node(nodeEl)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if nodeEl < current.data:
                if current.left is None:
                    current.left = Node(nodeEl)
                    break
                else:
                    queue.append(current.left)
            
            if nodeEl > current.data:
                if current.right is None:
                    current.right = Node(nodeEl)
                    break
                else:
                    queue.append(current.right)

    
    
    def search(self, rootNode, val):
        if rootNode is None:
            return None
        
        queue = [rootNode]
        while queue:
            currentRootEl = queue.pop(0)
            if currentRootEl.data == val:
                self.preOrder(currentRootEl)
                # return currentRootEl.data
            if val < currentRootEl.data:
                if currentRootEl.left is not None:
                    queue.append(currentRootEl.left)
            if val > currentRootEl.data:
                if currentRootEl.left is not None:
                    queue.append(currentRootEl.right)
        return False
    
    def preOrder(self, rootNode):
        if rootNode is None:
            return
        print(rootNode.data, end=" -> ")
        self.preOrder(rootNode.left)
        self.preOrder(rootNode.right)

root = int(input("Enter the root element: "))
tree = BST(root)
nodes = int(input("Enter the number of Nodes: "))
for i in range(nodes):
    tree.insert(int(input("Enter the node value: ")))
# tree.bfs(tree.root)

tree.search(tree.root, int(input("Enter the Search Element: ")))