import numpy as np
import math
arr = [[0.001,1],[0.002,3],[0.003,3.5],[0.004,4], [0.005,6]]
arr = np.array(arr)


def compliance(n):
    angle = (arr[n+1][0]-arr[n][0]) / (arr[n+1][1]-arr[n][1])
    return math.tan(angle) / 1.05

print(compliance(1))
print(compliance(2))
print(compliance(3))