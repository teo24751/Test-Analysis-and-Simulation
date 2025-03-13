import numpy as np
import math
import readData as rd
import matplotlib.pyplot as plt

array = rd.load_displacement_curve(3)

arr = [[0.001,1],[0.002,3],[0.003,3.5],[0.004,4], [0.005,6]]
arr = np.array(arr)



def compliance(n,arr):
    angle = (arr[n+2][0]-arr[n][0]) / (arr[n+2][1]-arr[n][1])
    return math.tan(angle) / 1.05

compl = []

for i in range(len(array)-2):
    compl.append(compliance(i,array))
print(compl)
#for i in range(int(len(compl)/5)+20):
    #print(compl[i])

def calculate_compliance():
    return compl
