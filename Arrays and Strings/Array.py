class Array:
    def __init__(self, n):
        self.data = []
        self.maxNumber = n

    def append(self, n):
        if len(self) < n:
            self.data.append(n)
        else:
            raise ValueError("array has reached max number of elements it can fill!")
    def pop(self):
        if len(self) == 0:
            raise ValueError("array is empty!")
        else:
            return self.data.pop()
    def get(self, index):
        if self.maxNumber < index or index < 0:
            raise IndexError("index is not a value between 0 and the specified array length!")
        else:
            return self.data[index]
