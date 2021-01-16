from Graph import Graph
from Node import Node
from Queue import Queue
#import random

graph = Graph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.addNeighbor(node2)
node1.addNeighbor(node3)

node2.addNeighbor(node4)

node3.addNeighbor(node4)
node3.addNeighbor(node5)

node4.addNeighbor(node6)

node5.addNeighbor(node6)

node7.addNeighbor(node8)

node8.addNeighbor(node7)

nodes = [node1, node2, node3, node4, node5, node6, node7, node8]

graph.nodes = nodes

print(graph)

# bfs print implementation

def bfs(start, visited): # visited is a list that contains all the elements that have already been visited - this increases the space complexity since a better way can be to give the Node class a state value that determines if the node is visited or not
    visited.append(start)
    queue = Queue()
    queue.enqueue(start)
    while len(queue) != 0:
        current = queue.dequeue()
        print(current.data, end = " ")
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.append(neighbor)
        
def printNodes(graph):
    visited = [] # this is inefficient, but whatever
    for node in graph.nodes:
        if node not in visited:
            bfs(node, visited)

printNodes(graph)