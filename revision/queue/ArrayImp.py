class Queue:
    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def enqueue(self, data):
        if self.rear == self.capacity - 1:
            print("Queue is fulll")
        elif self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            poped = self.queue[self.front]
            self.front = self.rear == -1
        else:
            poped = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
        return poped
    
    def getFront(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
        else:
            print(self.queue[self.front])

    def getRear(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
        else:
            print(self.queue[self.rear])

