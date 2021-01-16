# adjacency list implementation
from Graph import Graph
from Node import Node
import random

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

#for i in range(5):
#    graph.addNode(i)

#print(graph)

#random = random.randint(0, 4)


#for i in range(20):
#    graph.addNeighbor(graph.nodes[random.randint(0, 4)], graph.nodes[random.randint(0, 4)])
#print(graph)

def dfsVisit(node, visited): # visited is a list that contains all the elements that have already been visited - this increases the space complexity since a better way can be to give the Node class a state value that determines if the node is visited or not
    visited.append(node)
    print(node.data, end = " ")
    for newNode in node.neighbors:
        if newNode not in visited:
            dfsVisit(newNode, visited)

def printNodes(graph):
    visited = [] # this is inefficient, but whatever
    for node in graph.nodes:
        if node not in visited:
            dfsVisit(node, visited)

printNodes(graph)


# make a deep copy of a graph

def dfsCopy(node, nodesDict):
    nodesDict[node] = Node(node.data)
    for newNode in node.neighbors:
        if newNode not in nodesDict:
            dfsCopy(newNode, nodesDict)
        nodesDict[node].neighbors.append(nodesDict[newNode])

def copyGraph(graph):
    nodesDict = {}
    aNewGraph = Graph()
    for node in graph.nodes:
        if node not in nodesDict:
            dfsCopy(node, nodesDict)
    for node in nodesDict:
        aNewGraph.nodes.append(nodesDict[node])
    return aNewGraph

copied = copyGraph(graph)
print()
printNodes(copied)
print()
node9 = Node(9)
node10 = Node(10)
graph.nodes.append(node9)
graph.addNeighbor(node1, node9)
graph.nodes[1].data = 11
copied.nodes.append(node10)
copied.addNeighbor(copied.nodes[0], node10)

print(graph)
print()
print(copied)