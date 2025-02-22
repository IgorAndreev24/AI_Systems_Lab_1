import numpy as np
import possibleMoves
from copy import deepcopy
import heapq


class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def arrayToTuple(array):
    return tuple(array.flatten())


def findPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]


def manhattanDistance(state, target):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:  # Ignore the blank tile
                targetRow, targetCol = np.where(target == tile)
                distance += abs(i - targetRow[0]) + abs(j - targetCol[0])
    return distance


def aStarSearch(matrix, target):
    initialHeuristic = manhattanDistance(matrix, target)
    startNode = Node(matrix, cost=0, heuristic=initialHeuristic)
    openQueue = [(initialHeuristic, startNode)]
    heapq.heapify(openQueue)

    visitedStates = {arrayToTuple(matrix)}
    costSoFar = {arrayToTuple(matrix): 0}
    iterationCount = 0

    while openQueue:
        iterationCount += 1
        fValue, currentNode = heapq.heappop(openQueue)

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
            newCost = currentNode.cost + 1
            heuristic = manhattanDistance(move, target)

            if moveTuple not in costSoFar or newCost < costSoFar[moveTuple]:
                costSoFar[moveTuple] = newCost
                newNode = Node(move, parent=currentNode, cost=newCost, heuristic=heuristic)
                heapq.heappush(openQueue, (newCost + heuristic, newNode))
                visitedStates.add(moveTuple)

    print("Решение не найдено")
    print("Количество итераций:", iterationCount)
