class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = self.rear = newNode
            
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.rear.next = self.front

    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Empty")
            return
        elif self.front == self.rear:
            poped = self.front.data
            self.front = self.rear = None
        else:
            poped = self.front.data
            self.front = self.front.next
            self.rear.next = self.front

    def peek(self):
        if self.front is None:
            print("Empty")
            return
        print(self.front.data)

    def rear(self):
        if self.front is None and self.rear is None:
            print("Empty")
            return
        print(self.rear.data)