# test implementation of stack
from stack import Stack

stack = Stack()
#stack.push(1)
#stack.push(2)
#stack.push(4)
#print(len(stack))
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(len(stack))
#print(stack.pop())
#print(len(stack))


def find(stack, num):
    temp = Stack()
    found = False
    while not stack.isEmpty():
        top = stack.peek()
        if top == num:
            found = True
            break
        temp.push(stack.pop())
    while not temp.isEmpty():
        stack.push(temp.pop())
    return found


#stack.push(1)
#stack.push(2)
#stack.push(4)
#print(find(stack, 3))
#print(find(stack, 4))
#print(find(stack, 1))
#print(find(stack, 2))
#print(find(stack, 5))

# test stack implementation of queue
from queue import Queue
q = Queue()

q.push(1)
q.push(2)
q.push(4)
print(len(q)) # should be 3
print(q.pop()) # should be 1 instead of 4
print(q.pop()) # should be 2
print(q.pop()) # should be 4
print(q.pop()) # should be None
print(q.pop()) # should be None