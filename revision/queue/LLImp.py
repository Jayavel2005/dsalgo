class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
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
    
    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Queue is empty.")
        else:
            poped = self.front.data
            self.front = self.front.next
        return poped
    

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return
        else:
            print(self.front.data)

    def rear(self):
        if self.rear is None:
            print("Queue is empty.")
            return
        else:
            print(self.rear.data)