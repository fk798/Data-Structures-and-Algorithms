# adjacency list implementation
from Graph import Graph
from Node import Node
import random

graph = Graph()

for i in range(5):
    graph.addNode(i)

#print(graph)

#random = random.randint(0, 4)


for i in range(20):
    graph.addNeighbor(graph.nodes[random.randint(0, 4)], graph.nodes[random.randint(0, 4)])
print(graph)