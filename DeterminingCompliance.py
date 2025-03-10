import numpy as np
import math
import readData as rd

array = rd.load_displacement_curve(3)

arr = [[0.001,1],[0.002,3],[0.003,3.5],[0.004,4], [0.005,6]]
arr = np.array(arr)

#for i in range(4):
    #print(array[i+53])


def compliance(n,arr):
    angle = (arr[n+2][0]-arr[n][0]) / (arr[n+2][1]-arr[n][1])
    return math.tan(angle) / 1.05

compl = []

for i in range(len(array)-1):
    compl.append(compliance(i,array))

print(compl)

