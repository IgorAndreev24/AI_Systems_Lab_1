from copy import deepcopy
import numpy as np

def move(matrix):
    moveList = []
    zeroIndex = np.where(matrix == 0)
    x = zeroIndex[0][0]
    y = zeroIndex[1][0]

    if(x < 2):
        copyMatrix = deepcopy(matrix)
        copyMatrix[x][y], copyMatrix[x + 1][y] = copyMatrix[x + 1][y], copyMatrix[x][y]
        moveList.append(copyMatrix)

    if(x > 0):
        copyMatrix = deepcopy(matrix)
        copyMatrix[x][y], copyMatrix[x - 1][y] = copyMatrix[x - 1][y], copyMatrix[x][y]
        moveList.append(copyMatrix)

    if(y < 2):
        copyMatrix = deepcopy(matrix)
        copyMatrix[x][y], copyMatrix[x][y + 1] = copyMatrix[x][y + 1], copyMatrix[x][y]
        moveList.append(copyMatrix)

    if(y > 0):
        copyMatrix = deepcopy(matrix)
        copyMatrix[x][y], copyMatrix[x][y - 1] = copyMatrix[x][y - 1], copyMatrix[x][y]
        moveList.append(copyMatrix)

    return moveList
