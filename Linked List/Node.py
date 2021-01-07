class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def disconnect(self):
        self.data = None
        self.next = None