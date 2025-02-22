import numpy as np
import possibleMoves
from copy import deepcopy

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def arrayToTuple(array):
    return tuple(array.flatten())

def findPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]

def depthFirstSearch(matrix, target):
    stack = [Node(matrix)]
    visitedStates = {arrayToTuple(matrix)}
    iterationCount = 0

    while stack:
        iterationCount += 1
        currentNode = stack.pop()
        currentState = currentNode.state

        if np.array_equal(currentState, target):
            print("Решение найдено!")
            path = findPath(currentNode)
            print("Количество ходов:", len(path) - 1)
            print("Количество итераций:", iterationCount)
            print("Целенаправленность перебора: ", (len(path) - 1) / iterationCount)
            print("Показать путь? Y/N:")
            while (1):
                ch = input()
                if (ch == "Y"):
                    for p in path:
                        print(p)
                    return
                elif (ch == "N"):
                    return
            break

        moveList = possibleMoves.move(currentState)
        for move in moveList:
            moveTuple = arrayToTuple(move)
            if moveTuple not in visitedStates:
                visitedStates.add(moveTuple)
                stack.append(Node(move, parent=currentNode))

    print("Решение не найдено")
    print("Количество итераций:", iterationCount)
