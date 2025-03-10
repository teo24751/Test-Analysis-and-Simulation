import numpy as np
import scipy as sp
import main
import readData
import matplotlib.pyplot as plt
import math

def f(x):
    return ((2+x)*(0.886+4.64*x-13.32*x**2+14.72*x**3-5.6*x**4))/(1-x)**1.5

def K_Q(P_Q,thickness,width,x):
    return P_Q/thickness/math.sqrt(width)*f(x)

def phi(x):
    return (1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4)*(1-x)/((19.118-5.0244*x-69.678*x**2+82.16*x**3)*(1-x)+2*(1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4))

def energy_integration(loads,displacements):
    return np.trapz(loads, x=displacements, axis=-1)

def G_Q(thickness,width,loads,displacements,x):
    return
#Initial values
print(readData.load_displacement_curve(3))
width=1
thickness=1
loads=readData.load_displacement_curve(3)[0]#np.array([11,12,13,14,17,20,36,45,77,80])
displacements=readData.load_displacement_curve(3)[1]
crack_lengths=readData.load_displacement_curve(3)[2]
x=crack_lengths/width

#Plotting the data to check if it's correct
plt.plot(displacements,loads)
plt.show()


#Linearization of the load-displacement curve
#Only a part of the data falls on the linear part of the curve - LS regression
initial_linear_index=2
final_linear_index=8

print(loads)
print(displacements)
new_loads=loads[initial_linear_index:final_linear_index]
new_displacements=displacements[initial_linear_index:final_linear_index]
print(new_loads)
print(new_displacements)

matrix=np.matrix([[final_linear_index-initial_linear_index,np.sum(new_displacements)],[np.sum(new_displacements),np.sum(new_displacements**2)]])
print(matrix)
vector_values=np.matrix([[np.sum(new_loads)],[np.sum(new_loads*new_displacements)]])
line_parameters=np.dot(np.linalg.inv(matrix),vector_values)
print('Line parameters: ', line_parameters)

offset_line_parameters=np.matrix([[line_parameters[0,0]],[line_parameters[1,0]/1.05]])
print('Offset line parameters: ',offset_line_parameters)
linearized_loads=offset_line_parameters[0,0]+offset_line_parameters[1,0]*displacements
print('Linearized loads',linearized_loads)
differences=loads-linearized_loads
differences=list(differences)[1:]
print(differences)

intersection_point_index=differences.index(min(differences))
intersection_load=loads[intersection_point_index]
intersection_displacement=displacements[intersection_point_index]
print(intersection_load)


#Now the appropriate load has to be determined:
if intersection_load/max(loads)>1.1:
    print('The test is invalid!')
elif intersection_displacement<>:

else:
    P_Q=intersection_load