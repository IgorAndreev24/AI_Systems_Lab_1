import numpy as np
import possibleMoves

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def arrayToTuple(array):
    return tuple(array.flatten())

def find_path(node):  # Востанавливаем путь от начального сотояния
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]  # Инвертируем путь, чтобы получить правильный порядок

def totalOverdoing(matrix,target):
    # Объявление списков
    Open = []
    Close = []

    # Заменяем append списком с первым элементом
    Open = [Node(matrix)]
    iterationCount = 0
    visitedStates = {arrayToTuple(matrix)}  # Инициализация множества посещенных состояний

    while Open:
        # Подсчет количества итераций
        iterationCount += 1
        currentNode = Open.pop(0)  # FIFO
        Close.append(currentNode.state)  # Добавляем состояние в список Close

        if np.array_equal(currentNode.state, target):
            print("Решение найдено!")
            path = find_path(currentNode)
            print("Количество необходимых ходов: ", len(path) - 1)
            print("Количество итераций: ", iterationCount)
            print("Целенаправленность перебора: ", (len(path) - 1) / iterationCount)
            print("Показать путь? Y/N:")
            while (1):
                if (input() == "Y"):
                    for p in path:
                        print(p)
                    return
                elif (input() == "N"):
                    return
            break

        moveList = possibleMoves.move(currentNode.state)

        for move in moveList:
            moveTuple = arrayToTuple(move)
            if moveTuple not in visitedStates:
                Open.append(Node(move, parent=currentNode))
                visitedStates.add(moveTuple)

    else:
        print("Решение не найдено")
        print("Список Open:", Open)
        print("Список Close:", Close)
        print("Количество итераций: ", iterationCount)
