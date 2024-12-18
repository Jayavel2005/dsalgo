# Node Creation

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# y = Node(6)


# Singly linked list creation
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SLL:
    def __init__(self) -> None:
        self.head = None

    def creation(self):
        nodes = int(input("Enter the number of Nodes: "))
        for i in range(nodes):
            newNode = Node(int(input("Enter the Node Value: ")))
            
            if self.head is None:
                self.head = newNode
            
            else:
                current.next = newNode

            current = newNode 

    def traversal(self):
        current = self.head
        while current != None:
            print(current.data, end = " -> ")
            current = current.next

    def insert_front(self):
        nodes = int(input("Enter the nodes: "))
        for i in range(nodes):
            newNode = Node(int(input("Enter the Node value: ")))

            if self.head is None:
                self.head = newNode

            else:
                newNode.next = self.head
                self.head = newNode

    def insertion_end(self):
        nodes = int(input("Enter the Node count: "))
        for i in range(nodes):
            newNode = Node(int(input("Enter the Node Value: ")))


            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            current = newNode

    def at_point(self,position):
        newNode = Node(int(input("Enter the node value: ")))
        current = self.head
        if position == 0:
            newNode.next = self.head
            self.head = newNode
        for i in range(1,position - 1):
            current = current.next
        newNode.next = current.next
        current.next = newNode


    def del_front(self):
        if self.head is None:
            print("There is no node to be deleted.")
            return
        else:
            self.head = self.head.next

    def del_end(self):
        current = self.head
        if self.head is None:
            print("No item to be deleted.")
            return
        elif self.head.next is None:
            self.head = None
            return
        
        while current.next.next != None:
            current = current.next

        
        current.next = None

    def del_position(self,position):
        prev = None
        current = self.head
        if position == 1:
            self.del_front()
        for i in range(position - 1):
            prev = current
            current = current.next
        prev.next = current.next
        current.next = None
        del current


sll = SLL()
sll.creation()

# sll.at_point(int(input("Enter the position: ")))
sll.del_position(int(input('Enter delete position: ')))
sll.traversal()

