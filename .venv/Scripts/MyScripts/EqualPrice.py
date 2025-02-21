import numpy as np
import possibleMoves
from copy import deepcopy
import heapq  # приоритетная очередь

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        #  сравниваю для приоритетной очереди
        return self.cost < other.cost

def arrayToTuple(array):
    return tuple(array.flatten())

def findPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]

def uniformCostSearch(matrix, target):

    openQueue = []
    costSoFar = {arrayToTuple(matrix): 0}

    # добавляю начальную вершину в приоритетную очередь
    initialNode = Node(matrix, cost=0)
    heapq.heappush(openQueue, (0, initialNode))

    visitedStates = {arrayToTuple(matrix)}
    iterationCount = 0

    while openQueue:
        iterationCount += 1

        # получаю вершину с наименьшей стоимостью
        currentCost, currentNode = heapq.heappop(openQueue)
        currentState = currentNode.state

        if np.array_equal(currentState, target):
            print("Решение найдено!")
            path = findPath(currentNode)
            print("Количество ходов:", len(path) - 1)
            print("Количество итераций:", iterationCount)
            print("Целенаправленность перебора: ", (len(path) - 1) / iterationCount)
            print("Показать путь? Y/N:")
            while(1):
                if(input() == "Y"):
                    for p in path:
                        print(p)
                    return
                elif (input() == "N"):
                    return

        moveList = possibleMoves.move(currentState)

        for move in moveList:
            moveTuple = arrayToTuple(move)
            newCost = currentCost + 1  # предполагаю что каждый ход имеет стоимость 1

            if moveTuple not in costSoFar or newCost < costSoFar[moveTuple]:
                costSoFar[moveTuple] = newCost
                newNode = Node(move, parent=currentNode, cost=newCost)
                heapq.heappush(openQueue, (newCost, newNode))
                visitedStates.add(moveTuple)

    print("Решение не найдено")
    print("Количество итераций:", iterationCount)
