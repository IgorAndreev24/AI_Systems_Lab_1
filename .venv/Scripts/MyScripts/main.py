import numpy as np
import possibleMoves

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

# Объявление списков
Open=[]
Close = []
matrix = np.array([[1, 2, 3],
                   [8, 6, 4],
                   [0, 7, 5]])
target = np.array([[1, 2, 3],
                   [8, 0, 4],
                   [7, 6, 5]])

def arrayToTuple(array):
    return tuple(array.flatten())
# Заменяем append списком с первым элементом
Open = [Node(matrix)]
iterationCount = 0
visitedStates = {arrayToTuple(matrix)}  # Инициализация множества посещенных состояний

def find_path(node): # Востанавливаем путь от начального сотояния
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]  # Инвертируем путь, чтобы получить правильный порядок

while Open:
    # Подсчет количества итераций
    iterationCount += 1
    currentNode = Open.pop(0)  # FIFO
    Close.append(currentNode.state)  # Добавляем состояние в список Close

    if np.array_equal(currentNode.state, target):
        print("Решение найдено!")
        path = find_path(currentNode)
        for p in path:
            print(p)
        print("Количество необходимых ходов: ", len(path))
        print("Количество итераций: ", iterationCount)
        print("Целенаправленность перебора: ", len(path)/iterationCount)
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
