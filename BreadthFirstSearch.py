from Node import *
from MyQueue import *

def BreadthFirstSearch(graph, nodeData):
    visited = []
    currentQueue : MyQueue = MyQueue()
    BreadthFirstSearch2(visited, graph, nodeData, currentQueue)

def BreadthFirstSearch2(visisted, graph, nodeData, currentQueue : MyQueue):
    visisted.append(nodeData)
    currentQueue.add(nodeData)

    while currentQueue.isEmpty() == False:
        currentNodeData = currentQueue.remove() #returns node data
        print(currentNodeData)

        for neighbor in graph[currentNodeData]:
            if neighbor not in visisted:
                visisted.append(neighbor)
                currentQueue.add(neighbor)


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []

    }

    BreadthFirstSearch(graph, 'A')

if __name__ == '__main__':
    main()



