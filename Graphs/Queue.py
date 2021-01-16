# queue implementation for breadth first search
# queue is implemented using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def destroy(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def enqueue(self, data): # O(1) time implementation
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.length += 1
    
    def dequeue(self): # O(1) time implementation
        if self.head == None:
            print("Queue is empty")
            return None
        front = self.head
        self.head = self.head.next
        if self.head == None: # if there are no more elements left
            self.tail = None
        ret = front.data
        front.destroy()
        self.length -= 1
        return ret