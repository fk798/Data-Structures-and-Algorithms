from Node import Node

# directed graph
class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, data):
        node = Node(data)
        self.nodes.append(node)
        self.nodes.sort(key = lambda x: x.data)

    def addNeighbor(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            if node2 not in node1.neighbors:
                node1.addNeighbor(node2)

    def __str__(self):
        string = ""
        for i in range(len(self.nodes)):
            string += str(self.nodes[i]) + "\n"
        return string

    def __repr__(self):
        return str(self)