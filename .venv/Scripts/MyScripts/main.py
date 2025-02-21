import numpy as np
import possibleMoves
import TotalOverdoing
import EqualPrice

matrix = np.array([[1, 2, 3],
                   [8, 6, 4],
                   [0, 7, 5]])

target = np.array([[1, 2, 3],
                   [8, 0, 4],
                   [7, 6, 5]])

print("Running полный перебор:")
TotalOverdoing.totalOverdoing(matrix, target)

print("\nRunning метод равных цен:")
EqualPrice.uniformCostSearch(matrix, target)
