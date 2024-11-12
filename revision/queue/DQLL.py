class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def insertFront(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def insertLast(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def removeFront(self):
        if self.front is None:
            print("List is empty")
            return None
        elif self.front == self.rear:  # Only one element
            popped = self.front.data
            self.front = self.rear = None
        else:
            popped = self.front.data
            self.front = self.front.next
            self.front.prev = None
        return popped

    def removeLast(self):
        if self.rear is None:
            print("List is empty")
            return None
        elif self.front == self.rear:  # Only one element
            popped = self.rear.data
            self.front = self.rear = None
        else:
            popped = self.rear.data
            self.rear = self.rear.prev
            self.rear.next = None
        return popped

    def display(self):
        if self.front is None:
            print("List is empty")
            return
        current = self.front
        print("DLL elements from front to rear:")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
