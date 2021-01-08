# linked list implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def disconnect(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.data = None
        self.front = None
        self.back = None
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, n):
        if len(self) == 0:
            self.data = Node(n)
            self.front = self.data
            self.tail = self.data
        else:
            self.tail.next = Node(n)
            self.tail = self.tail.next
        self.length += 1
    
    def remove(self):
        if len(self) == 0:
            return None
        front = self.front
        res = front.data
        self.front = self.front.next
        front.disconnect()
        self.length -= 1
        return res

    def __str__(self):
        string = "Front <-- "
        front = self.front
        while front != self.back:
            string += str(front.data) + " <-- "
            front = front.next
        string += "Back"
        return string

    def __repr__(self):
        return str(self)

queue = Queue()
for i in range(1, 6):
    queue.add(i)
print(queue)

while len(queue) != 0:
    print(queue.remove())
    print(queue)