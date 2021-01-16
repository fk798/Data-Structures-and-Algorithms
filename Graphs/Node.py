class Node:
    def __init__(self, data):
        self.neighbors = []
        self.data = data
    
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
        self.neighbors.sort(key = lambda x: x.data)
    
    def __str__(self):
        return str(self.data) + " --> " +  str([self.neighbors[i].data for i in range(len(self.neighbors))])
    
    def __repr__(self):
        return str(self)

    """def __eq__(self, aNode):
        if self.data != aNode.data:
            return False
        if len(self.neighbors) != len(aNode.neighbors):
            return False
        for i in range(len(self.neighbors)):
            if self.neighbors[i].data != aGraph.neighbors[i].data:
                return False
        return True"""