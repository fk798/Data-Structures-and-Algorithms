# implement using lists b/c of circular queue - linked list implementation will be later

class Queue:
    MAX_DATA = 10
    def __init__(self):
        self.data = [None] * Queue.MAX_DATA
        self.front = 0 # front is the element to be popped
        self.back = 0 # back is the space that is next to be filled
        self.length = 0 # number of elements in the queue
    def __len__(self):
        return self.length
    
    def add(self, n):
        if len(self) == len(self.data): # if list is full, resize
            self.resize(len(self.data) * 2)
        self.data[self.back] = n 
        self.back = (self.back + 1) % len(self.data) # allows circularity
        self.length += 1

    def remove(self):
        if len(self) == 0: # nothing to remove
            return None
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.length -= 1
        if len(self) < len(self.data) // 4: # if the length of queue is 1/4 length of list
            self.resize(len(self.data) // 2) # halve the length of list
        return result

    def peek(self):
        if len(self) == 0:
            return None
        return self.data[self.front]

    def resize(self, num):
        old = self.data
        self.data = [None] * num
        oldFront = self.front
        #oldBack = self.back
        #counter = 0
        for indx in range(len(self)):
            self.data[indx] = old[oldFront]
            oldFront = (oldFront + 1) % len(old)
        self.front = 0 # restart from beginning of new list (in case there were spaces in the previous list)
        self.back = len(self)

        #while oldFront != oldBack:
        #    self.data[counter] = old[oldFront]
        #    oldFront = (oldFront + 1) % len(old)
        #    counter += 1
        #self.front = 0 # restart from beginning of new list (in case there were spaces in the previous list)
        #self.back = counter

    def __str__(self):
        string = "Front <-- "
        front = self.front
        back = self.back
        while front != back:
            string += str(self.data[front]) + " <-- "
            front += 1
        string += "Back"
        return string

    def __repr__(self):
        return str(self)

queue = Queue()
for i in range(1, 6):
    queue.add(i)
print(queue)
#print(queue.data)
while len(queue) != 0:
    print(queue.remove())
    #print(queue.data)
    print(queue)

print(queue.remove())
#print(queue.data)
print(queue)