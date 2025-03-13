import numpy as np
import scipy as sp
import main
import readData
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression

def f(x):
    return ((2+x)*(0.886+4.64*x-13.32*x**2+14.72*x**3-5.6*x**4))/(1-x)**1.5

def K_Q(P_Q,thickness,width,x):
    return P_Q/thickness/math.sqrt(width)*f(x)

#def fracture_toughness(displacements,loads,crack_lengths):
  #  return

def phi(x):
    return (1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4)*(1-x)/((19.118-5.0244*x-69.678*x**2+82.16*x**3)*(1-x)+2*(1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4))

def energy_integration(loads,displacements):
    return np.trapz(loads, x=displacements, axis=-1)

def G_Q(thickness,width,loads,displacements,x):
    return

#Initial values


sample_number=3
width=1
thickness=1
loads=list(readData.load_displacement_curve(sample_number)[:,0])
displacements=list(readData.load_displacement_curve(sample_number)[:,1])
#crack_lengths=np.array(readData.load_displacement_curve(sample_number)[:,2])
#x=crack_lengths/width


#Linearization of the load-displacement curve
#Only a part of the data falls on the linear part of the curve - LS regression
error_initial=1.1
error_final=1.1
initial_linear_index=18


final_linear_index=40
actual_length=len(loads[initial_linear_index:final_linear_index])
print(max(loads))

sums_of_residuals=[1000,1000]

counter=0
S=10000
while S>sums_of_residuals[-2] and counter<1000:
    counter+=1

    linear_part_loads=loads[initial_linear_index:final_linear_index]
    linear_part_displacements=displacements[initial_linear_index:final_linear_index]
    matrix=np.matrix([[final_linear_index-initial_linear_index+1,np.sum(linear_part_displacements)],[np.sum(linear_part_displacements),np.sum((np.array(linear_part_displacements)**2))]])
    vector_values=np.matrix([[np.sum(linear_part_loads)],[np.sum(np.array(linear_part_loads)*np.array(linear_part_displacements))]])
    line_parameters=np.dot(np.linalg.inv(matrix),vector_values)
    linearized_loads=list((np.array(linear_part_displacements))*(line_parameters[1,0])+np.array(line_parameters[0,0]))
    linearized_displacements=list(linear_part_displacements)
    error_initial=abs(linearized_loads[0]-loads[initial_linear_index])/loads[initial_linear_index]
    error_final=abs((linearized_loads[actual_length-1]-loads[final_linear_index]))/loads[final_linear_index]

    #Relative sum of residuals
    S=0
    for i in range(len(linear_part_loads)):
        S+=(linear_part_loads[i]-linearized_loads[i])
    S=S/len(linear_part_loads)
    

    if S>sums_of_residuals[-1]:
        initial_linear_index+=1
        final_linear_index-=1
        sums_of_residuals.append(S)
    else:
        break
    #if error_initial>2.0*10**(-1):
    #    
    #    actual_length-=1
    #if error_final>2.0*10**(-1): #Currently, the error is less than 5%
    #    
    #    actual_length-=1
        


linearized_loads=list((np.array(displacements))*(line_parameters[1,0])+np.array(line_parameters[0,0]))

offset_line_parameters=np.matrix([[line_parameters[0,0]],[line_parameters[1,0]/1.05]])
print('Offset line parameters: ',offset_line_parameters)
offset_loads=offset_line_parameters[0,0]+offset_line_parameters[1,0]*np.array(displacements)

plt.plot(displacements,loads)
plt.plot(displacements,linearized_loads)
plt.plot(displacements,offset_loads)
plt.show()

differences=abs(loads-linearized_loads)

print('Differences: ',differences)
print(min(differences))

intersection_load=loads[differences.index(min(abs(differences)))]
intersection_displacement=displacements[differences.index(min(abs(differences)))]
print(intersection_load)



#Now the appropriate load has to be determined:
#if intersection_load/max(loads)>1.1:
  #  print('The test is invalid!')
#elif intersection_displacement<>:

#else:
#    P_Q=intersection_load