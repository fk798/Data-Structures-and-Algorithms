# linked list implementation of a stack
from linkedlist import Node

# stack class implementation
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    # this is O(1)
    def __len__(self):
        return self.length
    
    # this is O(n) - can make it better by keeping track in init
    #def __len__(self):
    #    length = 0
    #    trav = self.head
    #    while trav:
    #        length += 1
    #        trav = trav.next
    #    return length

    def isEmpty(self):
        return len(self) == 0

    # LI
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1
    
    # FO
    def pop(self):
        # new implementation
        if len(self) == 0:
            return None
        ret = self.head.data
        temp = self.head.next
        del self.head
        self.head = temp
        self.length -= 1
        return ret

        # old implementation - terrible
        #ret = None
        #if self.head:
        #    ret = self.head.data
        #    temp = self.head.next
        #    #self.head.next = None # don't think this is needed
        #    del self.head
        #    self.head = temp
        #    self.length -= 1
        #return ret
    
    def peek(self):
        if len(self) != 0:
            return self.head.data
        return None

