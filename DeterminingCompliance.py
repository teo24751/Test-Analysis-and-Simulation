import numpy as np
import math
import readData as rd
import matplotlib.pyplot as plt

sample_number = 1

array = rd.load_displacement_curve(sample_number)
print(array[i][0] for i in range(0,50))
def compliance(n,arr):
    if (arr[n][1]-8.090e-04)/arr[n][0] > 0:
        return (arr[n][1]-8.090e-04)/arr[n][0]
    else:
        return 0

for i in range(50):
    print(array[i])

compl = []

#for i in range(int(len(compl)/5)+20):
    #print(array[i])
for i in range(6,len(array)-2):
    #print(i)
    compl.append(float(compliance(i,array)/1000))
#print(compl)



def calculate_compliance():
    return compl
