class EmptyCollection(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if(self.is_empty() == True):
            raise EmptyCollection("Stack is empty")
        return self.data.pop()

    def top(self):
        if(self.is_empty() == True):
            raise EmptyCollection("Stack is empty")
        return self.data[-1]

