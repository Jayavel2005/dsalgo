class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    
    def enqueue(self, data):
        if ((self.rear + 1) % self.capacity == self.front):
            print("It is full")
        elif self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == - 1 and self.rear == -1:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            poped = self.queue[self.front]
            self.queue[self.front] = None
        else:
            poped = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
        return poped
    
    def peek(self):
        if self.front == - 1 and self.rear == -1:
            print("Queue is empty.")
            return
        else:
            print(self.queue[self.front])

    def display(self):
        if self.front == - 1 and self.rear == -1:
            print("Queue is empty.")
            return
        i = self.front
        while(i != self.rear):
            print(self.queue[i])
            i = (i + 1) % self.capacity
        print(self.queue[self.rear])