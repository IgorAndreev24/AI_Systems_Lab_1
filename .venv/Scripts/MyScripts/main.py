import numpy as np
import possibleMoves
import TotalOverdoing
import EqualPrice
import DepthSearch
import AStarSearch

matrix = np.array([[1, 3, 6],
                   [5, 4, 7],
                   [0, 8, 2]])

target = np.array([[1, 2, 3],
                   [8, 0, 4],
                   [7, 6, 5]])

print("Running полный перебор:")
TotalOverdoing.totalOverdoing(matrix, target)

print("\nRunning метод равных цен:")
EqualPrice.uniformCostSearch(matrix, target)

print("\nRunning перебор в глубину:")
DepthSearch.depthFirstSearch(matrix, target)

print("\nRunning перебор А*:")
AStarSearch.aStarSearch(matrix, target)
