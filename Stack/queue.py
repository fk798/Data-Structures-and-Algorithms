# implement queue using stack
from stack import Stack

class Queue:
    def __init__(self):
        self.head = Stack()
        self.temp = Stack()

    def __len__(self):
        return len(self.head)
    
    def isEmpty(self):
        return len(self) == 0

    # FI - Enqueue
    def push(self, data):
        self.head.push(data)

    # FO - Dequeue
    def pop(self):

        # flushing helper method for pop
        def flush(stack1, stack2):
            while not stack1.isEmpty():
                stack2.push(stack1.pop())

        if len(self) == 0:
            return None
        temp = Stack()
        flush(self.head, temp)
        ret = temp.pop()
        flush(temp, self.head)
        return ret