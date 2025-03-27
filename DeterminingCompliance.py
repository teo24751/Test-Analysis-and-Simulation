import numpy as np
import math
import readData as rd
import matplotlib.pyplot as plt

sample_number = 2

array = rd.load_displacement_curve(sample_number)
print(array[i][0] for i in range(0,50))
def compliance(n,arr):
    return arr[n][1]/arr[n][0]


compl = []

#for i in range(int(len(compl)/5)+20):
    #print(array[i])
for i in range(6,len(array)-2):
    #print(i)
    compl.append(compliance(i,array)/1000)
#print(compl)


def calculate_compliance():
    return compl
