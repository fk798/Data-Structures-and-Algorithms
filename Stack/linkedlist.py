# node class for linked list
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head:
            trav = self.head
            while trav.next:
                trav = trav.next
            trav.next = node
        else:
            self.head = node

    def print(self):
        trav = self.head
        while trav:
            print(trav.data)
            trav = trav.next