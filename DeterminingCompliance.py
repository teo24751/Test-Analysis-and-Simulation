import numpy as np
import math
import readData as rd
import matplotlib.pyplot as plt

array = rd.load_displacement_curve(3)

arr = [[0.001,1],[0.002,3],[0.003,3.5],[0.004,4], [0.005,6]]
arr = np.array(arr)



def compliance(n,arr):
    return arr[n][1]/arr[n][0]

compl = []

#for i in range(int(len(compl)/5)+20):
    #print(array[i])
for i in range(6,len(array)-2):
    #print(i)
    compl.append(compliance(i,array))
print(compl)


def calculate_compliance():
    return compl
