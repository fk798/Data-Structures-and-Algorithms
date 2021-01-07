from Node import Node
import random

# no tail implementation, so everything is harder :)
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if type(data) == Node:
            node = data
        else:
            node = Node(data)
        if self.head == None:
            self.head = node
            return
        trav = self.head
        while trav.next != None:
            trav = trav.next
        trav.next = node

    def delete(self, data): # really redundant, could divide into two different functions for node and data value
        if self.head == None:
            return
        if type(data) == Node: # deleting a node
            if self.head == data:
                temp = self.head.next
                self.head.disconnect()
                self.head = temp
            else:
                trav = self.head
                while trav.next != None:
                    if trav.next == data:
                        temp = trav.next
                        trav.next = temp.next
                        temp.disconnect()
                        break
                    trav = trav.next
        else: # deleting first instance of a data value
            if self.head.data == data:
                temp = self.head.next
                self.head.disconnect()
                self.head = temp
            else:
                trav = self.head
                while trav.next != None:
                    if trav.next.data == data:
                        temp = trav.next
                        trav.next = temp.next
                        temp.disconnect()
                        break
                    trav = trav.next

    def get(self, n: int):
        trav = self.head
        for i in range(n - 1):
            if trav != None:
                trav = trav.next
        return trav
    
    def __str__(self):
        string = ""
        trav = self.head
        while trav:
            string += str(trav.data) + " --> "
            trav = trav.next
        string += "None"
        return string
    def __repr__(self):
        return str(self)

    # O(n) time, O(n) space bc of dictionary
    def sort(self):
        table = {}
        trav = self.head
        while trav:
            if trav.data in table:
                temp = trav.next
                trav.next = table[trav.data]
                table[trav.data] = trav
                trav = temp
                
            else:
                table[trav.data] = trav
                temp = trav.next
                trav.next = None
                trav = temp
        self.head = None
        for key in sorted(table.keys()):
            if self.head == None:
                self.head = table[key]
            else:
                trav = self.head
                while trav.next != None:
                    trav = trav.next
                trav.next = table[key]
        

alist = SinglyLinkedList()
for i in range(10):
    alist.append(random.randint(0, 100))

alist.append(Node(1))

toSort = SinglyLinkedList()
for i in range(10):
    toSort.append(random.randint(0, 2))

#print(toSort)

#toSort.sort()

#print(toSort)

#print(alist)

#print(alist.get(4).data)

# separate a linked list into one odd and one even linked list - by position, not value
# O(n) time, O(1) space
def separate(linkedlist):
    head = linkedlist.head
    linkedlist.head = None
    oddPositions = SinglyLinkedList()
    evenPositions = SinglyLinkedList()

    num = 1 # regular indexing, not cs indexing
    trav = head
    while trav:
        temp = trav
        trav = trav.next
        temp.next = None
        if num % 2 == 0:
            evenPositions.append(temp)
        else:
            oddPositions.append(temp)
        num += 1
    return (oddPositions, evenPositions)

#separated = separate(alist)
#print(separated[0])
#print(separated[1])
#print(alist)
#alist.delete(alist.head.next)
#print(alist)

#anotherlist = SinglyLinkedList()
#print(anotherlist)
#anotherlist.delete(3)
#print(anotherlist)

def isCycle(linkedlist):
    head = linkedlist.head
    slow = head
    fast = head.next
    while fast != None:
        fast = fast.next
        if fast == None:
            return False
        if fast == slow:
            return True
        fast = fast.next
        slow = slow.next
    return False

cycle = SinglyLinkedList()
for i in range(1, 6):
    cycle.append(i)
travCycle = cycle.head
while travCycle.next != None:
    travCycle = travCycle.next
travCycle.next = cycle.head.next

#print(isCycle(cycle))
travCycle = cycle.head
for i in range(12):
    print(str(travCycle.data) + " --> ", end="")
    travCycle = travCycle.next
print()

def lengthCycle(linkedlist):
    head = linkedlist.head
    slow = head
    fast = head.next
    while fast != None:
        fast = fast.next
        if fast == None:
            return 0
        if fast == slow:
            break
        fast = fast.next
        slow = slow.next
    if fast == None:
        return 0
    counter = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        counter += 1
    return counter

#print(lengthCycle(cycle))
#print(lengthCycle(alist))

def findCycleBeginning(linkedlist):
    length = lengthCycle(linkedlist)
    if length == 0:
        return linkedlist.head
    slow = linkedlist.head
    fast = slow
    for i in range(length):
        fast = fast.next
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast.data

print(findCycleBeginning(cycle))

def medianOfList(linkedlist): # assumes no cycle
    head = linkedlist.head
    if head == None:
        return None
    slow = head
    fast = head.next
    while fast != None:
        slow = slow.next
        fast = fast.next
        if fast == None:
            break
        fast = fast.next
    return slow
#print(alist)
#print(medianOfList(alist).data)